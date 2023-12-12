"""Module for taking input for maintenance related task"""
import logging
#local imports
from config.queries import Header
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from controllers.manager_controllers import ManagerControllers
from utils.common_helper import CommonHelper
from utils.app_decorator import error_handler
from utils.validations import InputValidations

logger = logging.getLogger('maintenance_views')

class MaintenanceViews:
    """
        Class that contains menu options for taking input from manager to perform maintenance operations
    """
    def __init__(self,user_id) -> None:
        self.user_id = user_id
        self.obj_common_helper = CommonHelper()
        self.obj_manager_controller = ManagerControllers()

    def input_send_asset(self) -> None:
        """ Method that takes input for sending asset for maintenance """

        data = self.obj_manager_controller.view_pending_issues()

        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
            return 
        
        issue_id = InputValidations.input_issue_id()
        if not self.obj_manager_controller.send_asset(issue_id, self.user_id):
            print(PromptConfig.NO_DATA_EXISTS)
            return
        
        else:
            print(PromptConfig.SEND_FOR_MAINTENANCE)
            logger.info("Asset send for maintenance")
        
    def input_recieve_asset(self) -> None:
        """ Method that recieves assets from maintenance """

        data = self.obj_manager_controller.display_maintenance_table()

        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
            return
        
        CommonHelper.display_table(data, Header.SCHEMA_MAINTENANCE_TABLE)
        maintenance_id = InputValidations.input_maintenance_id()
        if not self.obj_manager_controller.recieve_asset(maintenance_id):
            print(PromptConfig.NO_DATA_EXISTS)
            return
        
        else:
            print(PromptConfig.RECIEVE_FROM_MAINTENANCE)
            logger.info("Recive asset from maintenance")
    
    def display_issues(self) -> None:
        """ Method that diplays all the pending issues """

        data = self.obj_manager_controller.view_pending_issues()

        if not data:
           print(PromptConfig.NO_DATA_EXISTS)   
        else: 
            CommonHelper.display_table(data, Header.SCHEMA_PENDING_ISSUES)
        
    @error_handler
    def maintenance_menu(self) -> bool:
        """ Method that takes input to perform operations, along with error handler decorator """
        
        user_choice = input(PromptConfig.MAINTENANCE_PROMPT + "\n")
        
        if user_choice == "1" : 
            self.display_issues()
        elif user_choice == "2" :
            self.input_send_asset()
        elif user_choice == "3" :
            self.input_recieve_asset()
        elif user_choice == "4" :
            return True
        else :
            print(PromptConfig.INVALID_INPUT + "\n") 
            logger.info("Invalid input entered")
        
        return False
