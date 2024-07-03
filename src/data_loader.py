import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

class DataLoader:

    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Use .env for credentials
        DB_HOST = os.getenv('DB_HOST')
        DB_USER = os.getenv('DB_USER')
        DB_PWD = os.getenv('DB_PWD')
        DB_NAME = os.getenv('DB_NAME')
        self.database_conn = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}')

    def query(self, query_str):
        return pd.read_sql(query_str, self.database_conn)