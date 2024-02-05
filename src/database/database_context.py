'''Context Manager for the database'''

import logging
import os
import mysql.connector
from pathlib import Path
from dotenv import load_dotenv

from config.queries import Queries

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
logger = logging.getLogger('database_context')


class DatabaseContext:
    '''
    Class for contect manager of creating MySQL database connection, 
    opening database connection and closing connection each time
    '''

    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_DB = os.getenv('MYSQL_DB')

    def __init__(self) -> None:
        self.connection = None
        self.cursor = None
        try:
            self.connection = mysql.connector.connect(
                user = DatabaseContext.MYSQL_USER,
                password=DatabaseContext.MYSQL_PASSWORD,
                host=DatabaseContext.MYSQL_HOST

                )
            self.cursor = self.connection.cursor(dictionary=True)
            self.cursor.execute(Queries.CREATE_DATABASE.format(DatabaseContext.MYSQL_DB))
            self.cursor.execute(Queries.USE_DATABASE.format(DatabaseContext.MYSQL_DB))

        except Exception as error:
            logger.exception(error)
            raise mysql.connector.Error from error
        else:
            logger.debug("Connection established")

        self.connection = self.connection
        self.cursor = self.cursor


    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type or exc_tb or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
