MALE = 1
FEMALE = 2

NO = 0
YES = 1
REFUSED_TO_ANSWER = 8
UNKNOWN = 9

SEX = 'g5_02'
AGE = 'g5_04a'
INJURY_DURATION_CUTTOFF = 30
MATERNAL_AGE_LOWER = 12
MATERNAL_AGE_UPPER = 49
PERIOD_OVERDUE_CUTTOFF = 90
PROLONGED_DELIVERY_CUTTOFF = 1 # in days


class Rash(object):
    FACE = 1
    TRUNK = 2
    EXTREMITIES = 3
    EVERYWHERE = 4


class BellyPain(object):
    UPPER_BELLY = 1
    LOWER_BELLY = 2


class Adult(object):
    EPILEPSY = 'a1_01_8'
    FEVER = 'a2_02'
    PALE = 'a2_20'
    BREATHING_DIFFICULT = 'a2_36'
    BREATHING_FAST = 'a2_40'
    CHEST_PAIN = 'a2_43'
    BELLY_PAIN = 'a2_61'
    BELLY_PAIN_LOCATION1 = 'a2_63_1'
    BELLY_PAIN_LOCATION2 = 'a2_63_2'
    HEADACHES = 'a2_69'
    CONVULSIONS = 'a2_82'
    EXCESSIVE_VAGINAL_BLEEDING_1_WEEK = 'a3_06'
    PERIOD_OVERDUE = 'a3_07'
    PERIOD_OVERDUE_DAYS = 'a3_08'
    PREGNANT = 'a3_10'
    DURING_ABORTION = 'a3_12'
    EXCESSIVE_BLEEDING_DURING = 'a3_14'
    DURING_CHILDBIRTH = 'a3_15'
    LABOR_DURATION = 'a3_16'
    AFTER_ABORTION = 'a3_17'
    AFTER_CHILDBIRTH = 'a3_18'
    OFFENSIVE_VAGINAL_DISCHARGE = 'a3_20'
    EXCESSIVE_BLEEDING_AFTER = 'a3_19'
    ROAD_TRAFFIC = 'a5_01_1'
    FALL = 'a5_01_2'
    DROWNING = 'a5_01_3'
    POISONING = 'a5_01_4'
    BITE = 'a5_01_5'
    BURN = 'a5_01_6'
    NO_INJURY = 'a5_01_8'
    OTHER_INJURY = 'a5_01_9a'
    SELF_INFLICTED = 'a5_02'
    INFLICTED_BY_OTHER = 'a5_03'
    INJURY_DAYS = 'a5_04'
    FREE_TEXT_SUICIDE = 'a_7_11'


class Child(object):
    ILLNESS_DAYS = 'c1_21'
    FEVER = 'c4_01'
    LOOSE_STOOL = 'c4_06'
    COUGH = 'c4_12'
    BREATHING_DIFFICULT = 'c4_16'
    FAST_BREATHING = 'c4_18'
    INDRAWN_CHEST = 'c4_20'
    RASH = 'c4_30'
    RASH_LOCATION = 'c4_31_1'
    THIN_LIMBS = 'c4_35'
    FLAKING_SKIN = 'c4_38'
    HAIR_COLOR_CHANGE_RED_YELLOW = 'c4_39'
    PROTRUDING_BELLY = 'c4_40'
    LACK_OF_BLOOD = 'c4_41'
    RASH_COLOR_WHITISH = 'c4_43'
    ROAD_TRAFFIC = 'c4_47_1'
    FALL = 'c4_47_2'
    DROWNING = 'c4_47_3'
    POISONING = 'c4_47_4'
    BITE = 'c4_47_5'
    BURN = 'c4_47_6'
    NO_INJURY = 'c4_47_11'
    OTHER_INJURY = 'c4_47_8a'
    INFLICTED_BY_OTHER = 'c4_48'
    INJURY_DAYS = 'c4_49'
    FREE_TEXT_CANCER = 'c_6_2'
    FREE_TEXT_DIARRHEA = 'c_6_5'
    FREE_TEXT_FEVER = 'c_6_6'
    FREE_TEXT_PNEUMONIA = 'c_6_9'


class Neonate(object):
    NEVER_CRIED_MOVED_BREATHED = 'c1_15'
    NORMAL_SUCKLING = 'c3_12'
    STOPPED_NORMAL_SUCKLING = 'c3_13'
    NORMAL_SUCKLING_DAYS = 'c3_14'
    STOPPED_NORMAL_SUCKLING_DAYS = 'c3_15'
    OPEN_MOUTH = 'c3_16'
    CONVULSIONS = 'c3_25'
    UNRESPONSIVE = 'c3_33'
