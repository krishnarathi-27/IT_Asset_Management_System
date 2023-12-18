"""
    Module for taking user credentials as input.
    This module contains max login attempts which are reduced by each invalid login.
"""
import logging
import time
import maskpass

# local imports
from config.app_config import AppConfig
from config.log_prompts.logs_config import LogsConfig
from config.prompts.prompts import PromptConfig
from controllers.auth_controllers import AuthControllers

logger = logging.getLogger("auth_view")


class AuthViews:
    """
    Class containing max_login_attempts and method for taking user credentials for input.
    ...
    Attributes
    ----------
    login_attempts -> maximum login attempts for each user i.e 3
    """

    def __init__(self) -> None:
        self.__login_attempts = AppConfig.MAX_LOGIN_ATTEMPTS
        self.obj_auth_controller = AuthControllers()

    def login(self) -> None:
        """Method that takes user credentials as input"""

        print(PromptConfig.ATTEMPTS_MESSAGE)
        while True:
            if self.__login_attempts == 0:
                logger.debug(LogsConfig.LOG_LOGIN_EXHAUSTED)
                print(PromptConfig.ATTEMPTS_EXHAUSTED)
                self.__login_attempts = AppConfig.MAX_LOGIN_ATTEMPTS
                time.sleep(20)
                logger.info(LogsConfig.LOG_LOGIN_ATTEMPTS_RESETTING)
            else:
                username = input(PromptConfig.ENTER_USERNAME)
                input_password = maskpass.askpass(PromptConfig.ENTER_PASSWORD)
                is_valid_success = self.obj_auth_controller.validate_user(
                    username, input_password
                )

                if not is_valid_success:
                    logger.debug(LogsConfig.LOG_LOGIN_ATTEMPT_REDUCING)
                    self.__login_attempts -= 1
                    print(PromptConfig.INVALID_LOGIN.format(self.__login_attempts))
                else:
                    logger.debug(LogsConfig.LOG_LOGIN_ATTEMPTS_RESETTING)
                    self.__login_attempts = AppConfig.MAX_LOGIN_ATTEMPTS

            choice = input(PromptConfig.EXIT_SYSTEM_PROMPT).lower()
            if choice == "y":
                break
