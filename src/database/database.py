"""This Module provides all methods related for database operations"""
import pymysql
from flask import current_app as app
from pathlib import Path
from dotenv import load_dotenv

# local imports
from src.config.queries import Queries
from src.database.database_context import DatabaseContext

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

class Database:
    
    def create_all_table(self) -> None:
        '''creates table in database if not exists'''
        try:
            with DatabaseContext() as connection:
                cursor = connection.cursor()
                cursor.execute(Queries.CREATE_AUTHENTICATION_TABLE)
                cursor.execute(Queries.CREATE_ASSET_CATEGORY_TABLE)
                cursor.execute(Queries.CREATE_VENDOR_TABLE)
                cursor.execute(Queries.CREATE_MAPPING_TABLE)
                cursor.execute(Queries.CREATE_ASSET_TABLE)
                cursor.execute(Queries.CREATE_ISSUE_TABLE)
                cursor.execute(Queries.CREATE_TOKEN_TABLE)

        except pymysql.Error:
            print("hihihi")
            app.logger.info("Defection")

    def save_data(self, query: str, data: tuple = None) -> bool:
        '''saves data in database'''

        with DatabaseContext() as connection:
            cursor = connection.cursor()
            if not data:
                cursor.execute(query)
            else:
                cursor.execute(query, data)
            # cursor.execute('SELECT ROW_COUNT()')

            # rows_affected = cursor.fetchone()['ROW_COUNT()']
            # if rows_affected:
            #     return True
            # return False

    def fetch_data(self, query: str, data: tuple = None) -> list[dict]:
        '''reads data from database.'''

        with DatabaseContext() as connection:
            cursor = connection.cursor()
            if not data:
                cursor.execute(query)
            else:
                cursor.execute(query, data)

            return cursor.fetchall()
