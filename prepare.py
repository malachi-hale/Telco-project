import pandas as pd
import os
import env
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames; stratify on churn.
    return train, validate, test DataFrames.
    '''
    
    # splits df into train_validate and test using train_test_split() stratifying on churn to get an even mix of each churn, yes or no
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.has_churned)
    
    # splits train_validate into train and validate using train_test_split() stratifying on churn to get an even mix of each churn
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.has_churned)
    return train, validate, test

def prep_telco(df):
    '''
       this function will eliminate duplicates, make dummy columns, drop redundant columns, and convert monthly charges and total charges columns into numeric.
       We will also call upon the split_data function to split our data into train, validate, and test.
    '''
        
    ## First we will get rid of duplicate columns
    df = df.loc[:,~df.columns.duplicated()]
    
    ##Add a numeric columns for churned or didn't churn
    df['has_churned'] = df['churn'].replace({'No' : 0, 'Yes': 1})
    
    ##Add a numerical column for paperless billing
    df['paperless_billing_numeric'] = df['paperless_billing'].replace({'No' : 0, 'Yes': 1})
    
    ## Now we will substitute the object values for dummy values that are easier to process. 
    dummy_df = pd.get_dummies(df[['partner', 'dependents', 'gender', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']], drop_first=True)
    
    ##Concatenate our dummy values to our main Dataframe. 
    df = pd.concat([df, dummy_df], axis=1)
    
    ## Drop the redundant columns.
    df = df.drop(columns = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 'internet_service_type', 'payment_type', 'churn', 'paperless_billing'])
    
    ##Our column total_charges has some empty string values, so we will replace those values with a 0
    
    df["total_charges"] = df.total_charges.replace(" ", "0")
    
    ##Now we will convert the numbers in our total_charges and monthly_charges columns to floats. 
    df['total_charges'] = df.total_charges.astype(float)
    
    df['monthly_charges'] = df.monthly_charges.astype(float)
    
    ## Now we can split our data into train, validate, and test
    
     # split data into train, validate, test dfs
    train, validate, test = split_data(df)
    
    return train, validate, test