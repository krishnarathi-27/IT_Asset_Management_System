import logging
import sqlite3
#local imports
from config.logs_config.log_statements import LogStatements

logger = logging.getLogger('database_connection')

class DatabaseConnection:
    '''Class of context manager for database functions'''

    def __init__(self,host: str) -> None:
        '''initialises connection and host'''
        try:
            self.connection = None
            self.host = host
        except Exception as e:
            logging.error(LogStatements.log_error_connecting_database)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, *args, **kwargs):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __enter__(self) -> None:
        '''Method creates connection'''
        try:
            self.connection = sqlite3.connect(self.host)
            return self.connection
        except Exception as e:
            logging.error(LogStatements.log_error_connecting_database)
    
    def __exit__(self,exc_type : str,exc_value : str,exc_tb : str) -> None: 
        '''commits and closes connection'''
        if exc_tb or exc_type or exc_value:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
