"""Module for taking input for maintenance related task"""
import logging
from utils.common_helper import CommonHelper
from utils.app_decorator import error_handler
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from utils.validations import InputValidations
from controllers.manager_controllers import ManagerControllers

logger = logging.getLogger('maintenance_views')

class MaintenanceViews:
    """
        Class that contains menu options for taking input from manager to perform maintenance operations
        ...
        Attributes
        ----------
        obj_common_helper = object of class CommonHelper
        Methods
        -------
        maintenance_operations() -> containing loop for displaying maintenance menu
        maintenance_menu() -> contains menu options for taking input from manager
    """
    def __init__(self,user_id) -> None:
        self.user_id = user_id
        self.obj_common_helper = CommonHelper()
        self.obj_manager_controller = ManagerControllers()

    def input_send_asset(self) -> None:
        if not self.obj_manager_controller.view_pending_issues():
            print(PromptConfig.NO_DATA_EXISTS)
            return
        
        issue_id = InputValidations.input_issue_id()
        if not self.obj_manager_controller.send_asset(issue_id, self.user_id):
            print(PromptConfig.NO_DATA_EXISTS)
            return
        
    def maintenance_operations(self) -> None:
        """
            Method that contains loop for displaying track asset menu
            Parameters : self
            Return type : None
        """
        logger.info("Maintenance menu displayed")         
        while True:
            if self.maintenance_menu():
                break

    @error_handler
    def maintenance_menu(self) -> bool:
        """
            Method that takes input to perform operations, along with error handler decorator 
            Parameters : self
            Return type : bool
        """
        user_choice = input(PromptConfig.MAINTENANCE_PROMPT + "\n")
        if user_choice == "1" : 
            if not self.obj_manager_controller.view_pending_issues():
                print(PromptConfig.NO_DATA_EXISTS)
        elif user_choice == "2" :
            pass
        elif user_choice == "3" :
            pass
        elif user_choice == "4" :
            return True
        else :
            print(PromptConfig.INVALID_INPUT + "\n") 
            logger.info("Invalid input entered")
        
        return False
