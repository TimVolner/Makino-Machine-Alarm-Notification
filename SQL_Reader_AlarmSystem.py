import pandas as pd
import sqlalchemy
import os

def main():
    
    # MS SQL Server Config
    server = '<IP>'  # mssql is set up on localhost
    port = '1433'  # the port I opened to access mssql
    database = '<NAME>'
    username = '<USER>'
    password = '<PASS>'
    driver = 'SQL+SERVER'
    schema = 'dbo'
    
    try:
        
        # create a sqlAlchemy engine with the above credentials
        connection_str = f'mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?driver={driver}'
        engine = sqlalchemy.create_engine(connection_str)

        a = ['CNCAlarms', 'PMCAlarms']

        for i in a:
            # read our mdf file!
            query = f'select * from {i};'
            df = pd.read_sql(query, engine)
            path = os.getcwd()
            file = path + '\\Data\\' + i
            df.to_csv(file, sep='\t', encoding='utf-8')
    
    except:
        pass