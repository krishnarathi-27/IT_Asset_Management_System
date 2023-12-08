"""Module for taking input from employee for various functionalities"""
import logging
from utils.app_decorator import error_handler
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from utils.validations import InputValidations
from controllers.employee_controllers import EmployeeControllers

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
        self.obj_emp_controller = EmployeeControllers()

    def check_assets_assigned(self) -> None:
        if not self.obj_emp_controller.display_assets_assigned(self.user_id):
            print(PromptConfig.NO_DATA_EXISTS)

    def input_raise_issue(self) -> None:
        if not self.obj_emp_controller.display_assets_assigned(self.user_id):
            print(PromptConfig.NO_DATA_EXISTS)
            return
        
        asset_id = InputValidations.input_asset_id()
        if not self.obj_emp_controller.raise_issue(self.user_id, asset_id):
            print(PromptConfig.ASSET_ID_NOT_EXISTS)
            return 
        else:
            print(PromptConfig.ISSUE_RAISED)
    
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
            self.obj_emp_controller.display_employee_details(self.user_id)
        elif user_choice == "2" :
            self.check_assets_assigned()
        elif user_choice == "3" : 
            self.input_raise_issue()
        elif user_choice == "4" :
            return True
        else :
            print(PromptConfig.INVALID_INPUT + "\n") 
            logger.info("Invalid input entered")
        
        return False
    