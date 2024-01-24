"""Module contains common utility functions which are accessed across different modules"""
import logging
import hashlib
from tabulate import tabulate
from database.database import db
from config.queries import Queries
from utils.validations import InputValidations
from config.queries import Header
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
    def display_table(data: list, headers: list) -> None:
        """
        Method to display data in tabular format using tabulate
        Parameters : data, headers
        Return type : None
        """
        row_id = [i for i in range(1, len(data) + 1)]
        print(tabulate(data, headers, showindex=row_id, tablefmt="simple_grid"))

    def display_user_details(self) -> bool:
        """Method to display details of users"""

        data = db.fetch_data(Queries.FETCH_AUTHENTICATION_TABLE)

        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
            return False

        CommonHelper.display_table(data, Header.SCHEMA_USER_TABLE)
        return True
