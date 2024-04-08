'''Context Manager for the database'''
import pymysql
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import current_app as app

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

class DatabaseContext:
    '''
    Class for contect manager of creating MySQL database connection, 
    opening database connection and closing connection each time
    '''

    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_PORT = 19828

    def __init__(self) -> None:
        self.connection = None
        self.cursor = None
        try:
            timeout = 10
            self.connection = pymysql.connect(
                charset="utf8mb4",
                connect_timeout=timeout,
                cursorclass=pymysql.cursors.DictCursor,
                db="assetmanagement",
                host=DatabaseContext.MYSQL_HOST,
                password=DatabaseContext.MYSQL_PASSWORD,
                read_timeout=timeout,
                # port=DatabaseContext.MYSQL_PORT,
                user=DatabaseContext.MYSQL_USERNAME,
                write_timeout=timeout,
                )
            self.cursor = self.connection.cursor()

        except pymysql.Error as error:
            print(error.args)
            app.logger.exception(error)
            raise pymysql.Error from error
        else:
            app.logger.debug("Connection established")

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
