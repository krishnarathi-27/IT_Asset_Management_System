import pymysql
from flask import current_app as app

# local imports
from src.config.queries import Queries
from src.config.prompts.prompts import PromptConfig
from src.utils.exceptions import DBException

class ViewCategoryHandler:
    """
    Class containing buisness logic of methods to view both category from database
    """
    def __init__(self, db_object) -> None:
        self.db_object = db_object
        
    def view_all_category(self) -> dict:
        """Method to view al category from database"""
        app.logger.info('Viewing all categories')

        try:
            data = self.db_object.fetch_data(Queries.FETCH_CATEGORY_TABLE_WITH_VENDORS)
            return data
        
        except pymysql.Error as err:
            app.logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        