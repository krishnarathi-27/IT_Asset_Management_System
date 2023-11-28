import logging
import sqlite3
from prettytable import PrettyTable
#local imports
from config.queries_config.queries_config import ConfigQueries
from config.statements.statements import StatementsConfig
from database.database_connection import DatabaseConnection

logger = logging.getLogger('database_helper')

class DatabaseHelper:
    """Class containing methods for executing database queries"""

    def __init__(self) -> None:
        self.connection = sqlite3.connect('src\\database\\asset_management.db')
        self.cursor = self.connection.cursor()

    #@staticmethod
    def create_all_tables(self) -> None:
        # """Method for creating all tables of database"""
        # try:
        #     with DatabaseConnection(StatementsConfig.database_location) as connection:
        self.cursor.execute(ConfigQueries.create_authentication_table)
        self.cursor.execute(ConfigQueries.create_asset_category_table)
        self.cursor.execute(ConfigQueries.create_vendor_table)
        self.cursor.execute(ConfigQueries.create_mapping_table)
        self.cursor.execute(ConfigQueries.create_asset_table)
        self.cursor.execute(ConfigQueries.create_maintenance_table)
        self.cursor.execute(ConfigQueries.create_issue_table)
        # except sqlite3.Error as err:
        #     print(StatementsConfig.exception_message)
        #     logger.error(err) 

    # @staticmethod
    def save_data(self,query: str, tup: tuple) -> None:
        # '''Method to save data in the database'''
        # try:
        #     with DatabaseConnection(StatementsConfig.database_location) as connection:
        #cursor = connection.cursor()
        self.cursor.execute(query,tup) 
        # except sqlite3.Error as err:
        #     print(StatementsConfig.exception_message)
        #     logger.error(err) 

    # @staticmethod
    def fetch_data(self, query: str, tup: tuple = None) -> list:
        '''Method for fetching data from database '''
        # try:
        #     with DatabaseConnection(StatementsConfig.database_location) as connection:
        #         cursor = connection.cursor()
        if not tup:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query,tup)
        return self.cursor.fetchall() 
        # except sqlite3.Error as err:
        #     print(StatementsConfig.exception_message)
        #     logger.error(err) 

    # @staticmethod
    def display_data(self,query: str, table_schema: list, value: tuple = None) -> bool:
        '''Method for displaying data from database'''
        # try:
        #     with DatabaseConnection(StatementsConfig.database_location) as connection:
        #         cursor = connection.cursor()
        if not value:
            var = self.cursor.execute(query).fetchall()
        else:
            var = self.cursor.execute(query,value).fetchall()     
        if not any(var):
            print(StatementsConfig.no_data_exists)
            return False
        table = PrettyTable(table_schema)
        for row in var:
            table.add_row(row)
        print(table)
        return True
        # except sqlite3.Error as err:
        #     print(StatementsConfig.exception_message)
        #     logger.error(err) 
           
    # @staticmethod
    def delete_data(self, query: str, value: str) -> None:
        '''Method for deleting data from database '''
        # try:
        #     with DatabaseConnection(StatementsConfig.database_location) as connection:
        #         cursor = connection.cursor()
        self.cursor.execute(query,(value,))
        # except sqlite3.Error as err:
        #     print(StatementsConfig.exception_message)
        #     logger.error(err) 
    
db = DatabaseHelper()
