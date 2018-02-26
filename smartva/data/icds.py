from smartva.data.common_data import ADULT, CHILD, NEONATE


ICDS = {
    ADULT: {
        'AIDS': 'B24',
        'Bite of Venomous Animal': 'X27',
        'Breast Cancer': 'C50',
        'Cervical Cancer': 'C53',
        'Cirrhosis': 'K74',
        'Colorectal Cancer': 'C18',
        'Diabetes': 'E14',
        'Diarrhea/Dysentery': 'A09',
        'Drowning': 'W74',
        'Epilepsy': 'G40',
        'Esophageal Cancer': 'C15',
        'Falls': 'W19',
        'Fires': 'X09',
        'Homicide': 'Y09',
        'Leukemia/Lymphomas': 'C96',
        'Lung Cancer': 'C34',
        'Malaria': 'B54',
        'Maternal': 'O95',
        'Other Cardiovascular Diseases': 'I99',
        'Other Infectious Diseases': 'B99',
        'Other Injuries': 'X58',
        'Other Non-communicable Diseases': 'R100',
        'Pneumonia': 'J22',
        'Poisonings': 'X49',
        'Prostate Cancer': 'C61',
        'Renal Failure': 'N19',
        'Road Traffic': 'V89',
        'Stomach Cancer': 'C16',
        'Stroke': 'I64',
        'Suicide': 'X84',
        'TB': 'A16',
        'Chronic Respiratory': 'J44/45',
        'Ischemic Heart Disease': 'I24',
        'Other Cancers': 'C76',
        'Undetermined': 'R99',
    },
    CHILD: {
        'AIDS': 'B24',
        'Bite of Venomous Animal': 'X27',
        'Diarrhea/Dysentery': 'A09',
        'Drowning': 'W74',
        'Encephalitis': 'G04',
        'Falls': 'W19',
        'Fires': 'X09',
        'Hemorrhagic fever': 'A99',
        'Malaria': 'B54',
        'Measles': 'B05',
        'Meningitis': 'G03',
        'Cancers': 'C76',
        'Cardiovascular Diseases': 'I99',
        'Other Defined Causes of Child Deaths': 'R101',
        'Digestive Diseases': 'K92',
        'Other Infectious Diseases': 'B99',
        'Pneumonia': 'J22',
        'Poisonings': 'X49',
        'Road Traffic': 'V89',
        'Sepsis': 'A41',
        'Violent Death': 'Y09',
        'Undetermined': 'R99',
    },
    NEONATE: {
        'Birth asphyxia': 'P21',
        'Congenital malformation': 'Q89',
        'Meningitis/Sepsis': 'P36',
        'Pneumonia': 'P23/J22',
        'Preterm Delivery': 'P07',
        'Stillbirth': 'P95',
        'Undetermined': 'R99',
    },
}
