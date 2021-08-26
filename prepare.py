import pandas as pd
import os
import env
import matplotlib.pyplot as plt
import pandas as pd

def prep_telco(df):
    df = df.loc[:,~df.columns.duplicated()]
    dummy_df = pd.get_dummies(df[['partner', 'dependents', 'gender', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    df = df.drop(columns = ['customer_id', 'gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 'internet_service_type', 'payment_type'])
    return df