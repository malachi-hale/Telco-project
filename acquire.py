import os
import pandas as pd
import env
#We will connect to the SQL database
def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
     We establish a connection to the SQL database, using my information stored in the env file.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_telco_data():
    '''
    We will read a SQL query and create a file based on this query. I have also included a line to eliminate duplicate columns because value_counts() does not work if there are duplicate columns in the DataFrame.
    '''
    filename = "telco_churn.csv"
    ##We will write a SQL query to obtain the data
    sql = '''SELECT *
        FROM customers 
        JOIN contract_types
        ON contract_types.contract_type_id = customers.contract_type_id
        JOIN internet_service_types
        ON internet_service_types.internet_service_type_id = customers.internet_service_type_id
        JOIN payment_types 
        ON payment_types.payment_type_id = customers.payment_type_id'''
    ##If the file already exists we will simply pull the file.
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql(sql, get_connection('telco_churn'))
        ## We will get rid of duplicate columns that resulted from our SQL query
        df = df.loc[:,~df.columns.duplicated()]
        return df