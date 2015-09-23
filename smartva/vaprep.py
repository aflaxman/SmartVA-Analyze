import csv
import re
import os

from smartva.loggers import status_logger, warning_logger
from smartva.utils import status_notifier
from vaprep_data import (
    ADDITIONAL_HEADERS,
    SHORT_FORM_ADDITIONAL_HEADERS_DATA,
    BINARY_CONVERSION_MAP,
    AGE_HEADERS,
    ADULT_RASH_DATA,
    CHILD_WEIGHT_CONVERSION_DATA,
    FREE_TEXT_HEADERS,
    WORD_SUBS
)

ADULT = 'adult'
CHILD = 'child'
NEONATE = 'neonate'

PREPPED_FILENAME_TEMPLATE = '{:s}-prepped.csv'


def int_value(x):
    try:
        return int(x)
    except ValueError:
        return 0


class VaPrep(object):
    """
    This file cleans up input and converts from ODK collected data to VA variables.
    """

    def __init__(self, input_file, output_dir, short_form):
        self.input_file_path = input_file
        self.output_dir = output_dir
        self.short_form = short_form
        self.want_abort = False

        self._matrix_data = {
            ADULT: [],
            CHILD: [],
            NEONATE: []
        }

    @staticmethod
    def additional_headers_and_values(headers, additional_headers_data):
        """
        Calculate necessary additional headers and values based on comparing existing headers to additional header data.

        :param headers:
        :return:
        """
        additional_headers = []
        additional_values = []
        for k, v in additional_headers_data:
            if k not in headers:
                additional_headers.append(k)
                additional_values.append(v)

        return additional_headers, additional_values

    def run(self):
        status_notifier.update({'progress': (1,)})

        status_logger.debug('Initial data prep')

        with open(self.input_file_path, 'rU') as f:
            if self.want_abort:
                return False

            reader = csv.reader(f)

            # Read headers and check for free text columns
            headers = next(reader)

            # Extend the headers with additional headers and read the remaining data into the matrix
            additional_headers, additional_values = self.additional_headers_and_values(
                headers, [(k, 0) for k in ADDITIONAL_HEADERS] + SHORT_FORM_ADDITIONAL_HEADERS_DATA)
            headers.extend(additional_headers)

            for row in reader:
                new_row = row + additional_values

                self.convert_age_data(new_row, headers, AGE_HEADERS)

                self.convert_binary_variables(headers, new_row, BINARY_CONVERSION_MAP)

                self.convert_rash_data(headers, new_row, ADULT_RASH_DATA)

                self.convert_weight_data(headers, new_row, CHILD_WEIGHT_CONVERSION_DATA)

                self.convert_free_text(headers, new_row, FREE_TEXT_HEADERS, WORD_SUBS)

                self.save_row(headers, new_row)

        self.write_data(headers, self._matrix_data, self.output_dir)

        return True

    @staticmethod
    def convert_age_data(row, headers, age_headers):
        """
        Convert specified cells to int value or 0 if cell is empty.

        :param row:
        :param headers:
        :param age_headers:
        """
        # TODO: Eliminate this step in favor more robust future cell processing.
        for header in age_headers.values():
            row[headers.index(header)] = int_value(row[headers.index(header)])

    @staticmethod
    def convert_binary_variables(headers, row, conversion_data):
        """
        Convert multiple value answers into binary cells.

        :param headers:
        :param row:
        :param conversion_data:
        """
        for header in conversion_data:
            mapping = conversion_data[header]
            try:
                index = headers.index(header)
            except ValueError:
                # Header does not exist. Log a warning.
                warning_logger.debug('Skipping missing header "{}".'.format(header))
            else:
                for value in row[index].split(' '):
                    try:
                        if int(value) in mapping:
                            row[headers.index(mapping[int(value)])] |= 1
                    except ValueError:
                        # No values to process or not an integer value (invalid).
                        pass

    @staticmethod
    def convert_rash_data(headers, row, conversion_data):
        """
        Convert rash data into variables based on multiple choice questions.

        :param headers:
        :param row:
        :return:
        """
        for header in conversion_data:
            mapping = conversion_data[header]
            try:
                index = headers.index(header)
            except ValueError:
                # Header does not exist. Log a warning.
                warning_logger.debug('Skipping missing header "{}".'.format(header))
            else:
                try:
                    rash_values = map(int, row[index].split(' '))
                except ValueError:
                    # No rash data. Skip.
                    pass
                else:
                    if set(mapping['list']).issubset(set(rash_values)):
                        # if 1, 2, and 3 are selected, then change the value to 4 (all)
                        rash_values = [mapping['value']]
                    # set adultrash to the other selected values
                    for rash_index in range(min(len(rash_values), len(mapping['headers']))):
                        row[headers.index(mapping['headers'][rash_index])] = rash_values[rash_index]

    @staticmethod
    def convert_weight_data(headers, row, conversion_data):
        """
        Convert weights from kg to g.

        :param headers:
        :param row:
        :param conversion_data:
        :return:
        """
        for header in conversion_data:
            mapping = conversion_data[header]
            try:
                units = int(row[headers.index(header)])
            except ValueError:
                # No weight data. Skip.
                pass
            else:
                if units == 2:
                    weight = float(row[headers.index(mapping[units])]) * 1000
                    row[headers.index(header)] = 1
                    row[headers.index(mapping[1])] = weight

    @staticmethod
    def convert_free_text(headers, row, free_text_headers, word_subs):
        """
        Substitute words in the word subs list (mostly misspellings, etc..)

        :param headers:
        :param row:
        :param free_text_headers: Headers to process.
        :param word_subs: Dictionary of substution words.
        """
        for question in free_text_headers:
            try:
                index = headers.index(question)
            except ValueError:
                warning_logger.debug('Free text column "{}" does not exist.'.format(question))
            else:
                # check to see if any of the keys exist in the freetext (keys can be multiple words like 'dog bite')
                new_answer_array = []
                for word in re.sub('[^a-z ]', '', row[index].lower()).split(' '):
                    if word in word_subs:
                        new_answer_array.append(WORD_SUBS[word])
                    elif word:
                        new_answer_array.append(word)

                row[index] = ' '.join(new_answer_array)

    @staticmethod
    def get_age_data(headers, row):
        """
        Return age data in years, months, days, and module type.

        :param headers:
        :param row:
        :return: Age data in years, months, days, and module type.
        """
        age_data = {}
        for age, header in AGE_HEADERS.items():
            age_data[age] = int(row[headers.index(header)])

        return age_data

    @staticmethod
    def get_matrix(matrix_data, years=0, months=0, days=0, module=0):
        """
        Returns the appropriate age range matrix for extending.

        Adult = 12 years or older
        Child = 29 days to 12 years
        Neonate = 28 days or younger
        Module is used if age data are not used.

        :param matrix_data: Dictionary of age range matricies.
        :param years: Age in years
        :param months: Age in months
        :param days: Age in days
        :param module: Module, if specified
        :return: Specific age range matrix.
        :rtype : list
        """
        if years >= 12 or (not years and not months and not days and module == 3):
            return matrix_data[ADULT]
        if years or months or days >= 29 or (not years and not months and not days and module == 2):
            return matrix_data[CHILD]
        return matrix_data[NEONATE]

    def save_row(self, headers, row):
        """
        Save row of data in appropriate age matrix.

        :param headers:
        :param row:
        """
        self.get_matrix(self._matrix_data, **self.get_age_data(headers, row)).extend([row])

    @staticmethod
    def write_data(headers, matrix_data, output_dir):
        """
        Write intermediate prepped csv files.

        :param headers:
        """
        status_logger.debug('Writing adult, child, neonate prepped.csv files')

        for age, matrix in matrix_data.items():
            with open(os.path.join(output_dir, PREPPED_FILENAME_TEMPLATE.format(age)), 'wb', buffering=0) as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(matrix)

    def abort(self):
        self.want_abort = True
