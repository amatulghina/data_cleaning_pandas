import pandas as pd
import numpy as np


# Remove rows with missing values in all variables
def clean_missing(df):
    df.dropna(how='all', inplace=True)
    return df

# Cleaning invalid values

def clean_sex(df):
    df["sex"].replace(["M "," M","M x 2"], "M", inplace=True)
    df["sex"].replace(["lli","N","."], None , inplace=True)
    return df

def clean_age(df):
    df["age"].replace(["2 to 3 months", "9 months"], "0.5", inplace=True)
    df["age"].replace(["18 months"], "2", inplace=True)
    df["age"].replace(["2½"], "3", inplace=True)
    df["age"].replace(["6½", "7 or 8"], "7", inplace=True)
    df["age"].replace(["8 or 10", "9 or 10"], "9", inplace=True)
    df["age"].replace(["teen", "Teen", "a minor"], "10", inplace=True)
    df["age"].replace(["!!", "Both 11", "9 & 12", "10 or 12"], "11", inplace=True)
    df["age"].replace(["!2", "?    &   14", "12 or 13"], "12", inplace=True)
    df["age"].replace(["13 or 14"], "13", inplace=True)
    df["age"].replace(["!6", "13 or 18", "Teens", "16 to 18", "17 & 16"], "16", inplace=True)
    df["age"].replace(["18 or 20", "? & 19"], "19", inplace=True)
    df["age"].replace(["20?", "18 to 22", "20 "], "20", inplace=True)
    df["age"].replace(["23 & 20", "21 & ?"], "22", inplace=True)
    df["age"].replace(["20/30", "20s", "20's", "28 & 22", "7      &    31", "28 & 26", "21 or 26", "23 & 26", "mid-20s"], "25", inplace=True)
    df["age"].replace([" 28", "28, 23 & 30", "17 & 35", "25 or 28", "36 & 23", "34 & 19"], "28", inplace=True)
    df["age"].replace(["(adult)", "adult", '"middle-age"','"young"', "MAKE LINE GREEN", "9 & 60", "'young'", "young", " 30", "33 & 26", "45 and 15", "25 to 35", "F","", " ", "37, 67, 35, 27,  ? & 27", "21, 34,24 & 35"], "30", inplace=True)
    df["age"].replace(["30 & 32", "32 & 30"], "31", inplace=True)
    df["age"].replace(["Ca. 33", "X", "  ", "31 or 33", "22, 57, 31", "A.M.", "\xa0 "], "33", inplace=True)
    df["age"].replace(["30s", "M", "30 or 36", "33 or 37", "33 & 37", "mid-30s"], "35", inplace=True)
    df["age"].replace(["46 & 34", "50 & 30"], "40", inplace=True)
    df["age"].replace(["36 & 26"], "41", inplace=True)
    df["age"].replace([" 43"], "43", inplace=True)
    df["age"].replace(["40s", "45 "], "45", inplace=True)
    df["age"].replace(["50s"], "55", inplace=True)
    df["age"].replace(["60s", "60's", ">50"], "60", inplace=True)
    df["age"].replace(["74 ", "Elderly"], "74", inplace=True)
    df["age"] = shark_attacks["age"].astype(float)
    return df

def age_group(age):
    if age <= 12:
        return 'Child'
    elif age <= 20:
        return 'Teens'
    elif age <= 60:
        return 'Adult'
    else:
        return 'Senior'

def clean_activity(df):
    df["activity"] = df["activity"].apply(lambda x: x.lower() if isinstance(x, str) else x)
    df["activity"] = df["activity"].replace(r'.*fishing.*', 'fishing', regex=True)
    df["activity"] = df["activity"].replace(r'.*diving.*', 'diving', regex=True)
    df["activity"] = df["activity"].replace(r'.*surfing.*', 'surfing', regex=True)
    df["activity"] = df["activity"].replace(r'.*surf.*', 'surfing', regex=True)
    df["activity"] = df["activity"].replace(r'.*swimming.*', 'swimming', regex=True)
    df["activity"] = df["activity"].replace(r'.*wading.*', 'wading', regex=True)
    activity = ["fishing", "diving", "surfing", "swimming", "wading"]
    df.loc[~df["activity"].isin(activity), 'activity'] = 'other'
    return df

def clean_year(df):
    df["year"].replace([77], 1977, inplace=True)
    df["year"].replace([5,0], None, inplace=True)
    return df

def clean_injury(df):
    df["injury_type"] = df["injury"]
    df["injury_type"] = df["injury_type"].apply(lambda x: x.lower() if isinstance(x, str) else x)
    df["injury_type"] = df["injury_type"].replace(r'.*fatal.*', 'fatal', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*drown.*', 'fatal', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*no injury.*', 'survived', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*survived.*', 'survived', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*no inury.*', 'survived', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*bitten.*', 'injured', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*injury.*', 'injured', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*injuries.*', 'injured', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*foot.*', 'injured', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*leg.*', 'injured', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*lacerat.*', 'injured', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*severed.*', 'injured', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*injured.*', 'injured', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*bite.*', 'injured', regex=True)
    df["injury_type"] = df["injury_type"].replace(r'.*bitten.*', 'injured', regex=True)
    return df

def clean_type(df):
    df['type'] = df['type'].str.strip()
    replacements = {
        'Unverified': 'Questionable',
        'Under investigation': 'Questionable',
        'Unconfirmed': 'Questionable',
        '?': 'Questionable',
        'Boat': 'Watercraft',
        'Invalid': 'Questionable'
    }
    df['type'] = df['type'].replace(replacements)
    return df