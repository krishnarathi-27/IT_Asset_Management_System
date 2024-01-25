"""Module contains common utility functions which are accessed across different modules"""
import logging
import hashlib
from flask_smorest import abort

from database.database import db
from config.queries import Queries
from utils.validations import InputValidations
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger("common_helper")


class CommonHelper:
    """
    Class contains methods which are common and used across various files.
    """

    def change_default_password(self, username: str) -> None:
        """
        Method for changing default password of validated user
        Parameters : self, username
        Return type : None
        """

        while True:
            print(PromptConfig.STRONG_PASSWORD)
            new_password = InputValidations.input_password()
            print(PromptConfig.INPUT_CONFIRM_PASSWORD)
            confirm_password = InputValidations.input_password()

            if new_password != confirm_password:
                print(PromptConfig.PASSWORD_NOT_MATCH)

            else:
                new_hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                db.save_data(
                    Queries.UPDATE_DEFAULT_PASSWORD,
                    (
                        new_hashed_password,
                        username,
                    )
                )
                print(PromptConfig.DEFAULT_PASSWORD_UPDATED)
                logger.info(LogsConfig.LOG_DEFAULT_PASSWORD)
                return

    @staticmethod
    def server_error_handler(error: Exception):
        
        logger.exception(error)
        
        error_response = {
            "status_code": 500,
            "message": "Internal server erro occured. Try again after sometime"
        }

        return error_response
