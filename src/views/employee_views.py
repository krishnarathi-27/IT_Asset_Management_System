"""Module for taking input from admin for various functionalities"""
import logging
from utils.common_helper import CommonHelper
from utils.app_decorator import error_handler
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger('employee_views')

class EmployeeViews:
    """
        Class that contains menu options for taking input from employee to perform employee operations
        ...
        Attributes
        ----------
        obj_common_helper = object of class CommonHelper
        user_id = user id of the user that logged in the system
        Methods
        -------
        employee_operations() -> containing loop for displaying employee menu
        employee_menu() -> contains menu options for taking input from employee
    """
    def __init__(self,user_id) -> None:
        logger.info(LogsConfig.LOG_EMPLOYEE_LOGGED_IN)
        print(PromptConfig.WELCOME_EMPLOYEE)
        self.user_id = user_id
        self.obj_common_helper = CommonHelper()

    def employee_operations(self) -> None:
        """
            Method that contains loop for displaying employee menu
            Parameters : self
            Return type : None
        """
        logger.info("Employee menu displayed")
        while True:
            if self.employee_menu():
                break

    @error_handler
    def employee_menu(self) -> bool:
        """
            Method that takes input from employee to perform operations, along with error handler decorator 
            Parameters : self
            Return type : bool
        """
        user_choice = input(PromptConfig.EMPLOYEE_PROMPT + "\n")
        if user_choice == "1" : 
            pass
        elif user_choice == "2" :
            pass
        elif user_choice == "3" : 
            self.raise_issue()
        elif user_choice == "4" :
            return True
        else :
            print(PromptConfig.INVALID_INPUT + "\n") 
            logger.info("Invalid input entered")
        
        return False
    