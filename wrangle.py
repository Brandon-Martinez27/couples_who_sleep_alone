import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def wrangle_data():
    # read local `sleeping-alone-data.csv` to a dataframe
    df_prep = pd.read_csv('sleeping-alone-data.csv', encoding='ISO-8859-1')
    df_prep = df_prep.drop(columns=['StartDate', 'EndDate'],index=[0]).reset_index(drop=True)
    df_prep.columns = [col.lower() for col in df_prep.columns]
    df_prep = df_prep.dropna(axis=1, thresh=1000).dropna()
    
    new_col_names = ['status', 'rel_length', 'separate_bed', 
                 'occupation', 'gender', 'age', 'education', 'location']

    df_prep.columns = new_col_names

    ######### status #########
    ## Create 'Not Married' Category
    df_prep['status'] = np.where(
        df_prep['status'] != 'Married', 
        'Not Married', 
        df_prep['status'])

    ## ENCODE married
    # First I create a new dataframe that holds my encoded columns.
    married_dummies = pd.get_dummies(df_prep.status).drop(columns='Not Married')
    # Then I add my encoded columns back onto my original dataframe.
    df_prep = pd.concat([df_prep, married_dummies], axis=1).drop(columns='status')
    # lowercase col name
    df_prep = df_prep.rename(columns={'Married': 'married'})

    ######### rel_length #########
    ## Create '0-5 year' category
    df_prep['rel_length'] = np.where(
        df_prep['rel_length'] == 'Less than 1 year', 
        '0-5 years', 
        df_prep['rel_length'])

    df_prep['rel_length'] = np.where(
        df_prep['rel_length'] == '1-5 years', 
        '0-5 years', 
        df_prep['rel_length'])

    # Rename 'More than 20 years' to '20+ years'
    df_prep['rel_length'] = np.where(
        df_prep['rel_length'] == 'More than 20 years', 
        '20+ years', 
        df_prep['rel_length'])
    
    ######### separate_bed #########
    ## Create 'no' category
    df_prep['separate_bed'] = np.where(
        df_prep['separate_bed'] == 'Never', 
        0, 
        df_prep['separate_bed'])

    df_prep['separate_bed'] = np.where(
        df_prep['separate_bed'] == 'Once a year or less', 
        0, 
        df_prep['separate_bed'])

    df_prep['separate_bed'] = np.where(
        df_prep['separate_bed'] == 'Once a month or less', 
        0, 
        df_prep['separate_bed'])

    ## Create 'yes' category
    df_prep['separate_bed'] = np.where(
        df_prep['separate_bed'] == 'A few times per month', 
        1, 
        df_prep['separate_bed'])

    df_prep['separate_bed'] = np.where(
        df_prep['separate_bed'] == 'A few times per week', 
        1, 
        df_prep['separate_bed'])

    df_prep['separate_bed'] = np.where(
        df_prep['separate_bed'] == 'Every night', 
        1, 
        df_prep['separate_bed'])

    # change target to int type
    df_prep.separate_bed = df_prep.separate_bed.astype('int')

    ######### age #########
    # Rename '> 60' to '60+'
    df_prep['age'] = np.where(
        df_prep['age'] == '> 60', 
        '60+', 
        df_prep['age'])
    
    ######### education #########
    ## Create 'HS degree or less' category
    df_prep['education'] = np.where(
        df_prep['education'] == 'High school degree', 
        'HS degree or less', 
        df_prep['education'])

    df_prep['education'] = np.where(
        df_prep['education'] == 'Less than high school degree', 
        'HS degree or less', 
        df_prep['education'])
    
    ## ENCODE gender
    # First I create a new dataframe that holds my encoded columns.
    gender_dummies = pd.get_dummies(df_prep.gender).drop(columns='Female')
    # Then I add my encoded columns back onto my original dataframe.
    df_prep = pd.concat([df_prep, gender_dummies], axis=1).drop(columns='gender')
    # lowercase col name
    df_prep = df_prep.rename(columns={'Male': 'male'})

    return df_prep

def feature_engineering(df):
    df['long_term'] = np.where(
        (df['rel_length'] == '11-15 years') | (df['rel_length'] == '16-20 years'), 
        1, 
        0)

    df['young'] = np.where(
        (df['age'] == '18-29'), 
        1, 
        0)

    df['hs_or_less'] = np.where(
        (df['education'] == 'HS degree or less'), 
        1, 
        0)

    df['regional'] = np.where(
        ((df['location'] == 'East South Central') | 
        (df['location'] == 'Mountain') |
        (df['location'] == 'South Atlantic')), 
        1, 
        0)

    df['esc_610'] = np.where(
        ((df['location'] == 'East South Central') & 
        (df['rel_length'] == '6-10 years')), 
        1, 
        0)

    df['ma_1620'] = np.where(
        ((df['location'] == 'Middle Atlantic') & 
        (df['rel_length'] == '16-20 years')), 
        1, 
        0)

    df['mt_1115'] = np.where(
        ((df['location'] == 'Mountain') & 
        (df['rel_length'] == '11-15 years')), 
        1, 
        0)

    df['midage_hs'] = np.where(
        ((df['age'] == '30-44') & 
        (df['education'] == 'HS degree or less')), 
        1, 
        0)

    df['esc_bac'] = np.where(
        ((df['location'] == 'East South Central') & 
        (df['education'] == 'Bachelor degree')), 
        1, 
        0)

    df['pac_hs'] = np.where(
        ((df['location'] == 'Pacific') & 
        (df['education'] == 'HS degree or less')), 
        1,
        0)
    return df


def split_data(df):

    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.separate_bed)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.separate_bed)
    return train, validate, test

def encode_cat_vars(df, columns):
    for col in df[columns]:
        le = LabelEncoder().fit(df[col])
        df[col] = le.transform(df[col])
    return df