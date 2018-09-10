from sqlalchemy import create_engine
from config import parser

databaseHost = parser.get('DATABASE', 'HOST')
databaseUser = parser.get('DATABASE', 'USER')
databasePassword = parser.get('DATABASE', 'PASSWORD')
databaseName = parser.get('DATABASE', 'DATABASE_NAME')

connection_string = f'mssql+pyodbc://{databaseUser}:{databasePassword}@{databaseHost}/{databaseName}?driver=SQL+Server'

engine = create_engine(connection_string)
