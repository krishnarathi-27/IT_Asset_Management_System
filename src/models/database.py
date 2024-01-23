"""This Module provides all methods related for database operations"""
import os
import mysql.connector
import logging

from pathlib import Path
from dotenv import load_dotenv

from typing import Union

# local imports
from config.app_config import AppConfig
from config.queries import Queries
from config.log_prompts.logs_config import LogsConfig
from config.prompts.prompts import PromptConfig

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

logger = logging.getLogger(__name__)

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DB = os.getenv('MYSQL_DB')

class Database:
    """
    This class contains method to perform all database related operations
    ...
    Methods
    -------
    init() : To create connection and cursor
    create_all_tables() : To create all the table
    save_data() : To save data in database
    fetch_data() : TO fetch data from database
    """
    connection = None
    cursor = None

    def __init__(self) -> None:
        """
        This method creates sqlite connection and cursor
        Parameters = self
        Return Type = None
        """
        if Database.connection is None:
            try:
                Database.connection = mysql.connector.connect(
                    user = MYSQL_USER,
                    password=MYSQL_PASSWORD,
                    host=MYSQL_HOST

                    )
                Database.cursor = Database.connection.cursor(dictionary=True)
                Database.cursor.execute(Queries.CREATE_DATABASE.format(MYSQL_DB))
                Database.cursor.execute(Queries.USE_DATABASE.format(MYSQL_DB))
            except Exception as error:
                logger.exception(error)
                raise mysql.connector.Error from error
            else:
                logger.debug("Connection established")

        self.connection = Database.connection
        self.cursor = Database.cursor
        

    def create_all_table(self) -> None:
        """
        This method creates all tables of not exists
        Parameters = self
        Return Type = None
        """
        self.cursor.execute(Queries.CREATE_AUTHENTICATION_TABLE)
        self.cursor.execute(Queries.CREATE_ASSET_CATEGORY_TABLE)
        self.cursor.execute(Queries.CREATE_VENDOR_TABLE)
        self.cursor.execute(Queries.CREATE_MAPPING_TABLE)
        self.cursor.execute(Queries.CREATE_ASSET_TABLE)
        self.cursor.execute(Queries.CREATE_ISSUE_TABLE)

    def save_data(self, query: Union[str, list], data: Union[tuple, list]) -> None:
        """
        This saves data in the database
        Parameters = query that can we either string or list, tuple
        Return Type = None
        """
        if isinstance(query, str):
            self.cursor.execute(query, data)
        else:
            for i in range(0, len(query)):
                self.cursor.execute(query[i], data[i])
        self.connection.commit()

    def fetch_data(self, query: str, tup: tuple = None) -> list:
        """
        This fetches data in the database
        Parameters = query, tuple
        Return Type = List
        """
        if not tup:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, tup)
        data = self.cursor.fetchall()
        return data


db = Database()
