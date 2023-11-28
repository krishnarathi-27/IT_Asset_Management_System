import logging
import shortuuid
from os import system
#local imports
from config.prompts_config.prompts_config import PromptsConfig
from config.statements.statements import StatementsConfig
from config.queries_config.queries_config import ConfigQueries
from config.logs_config.log_statements import LogStatements
from database.database_helper import db
from utils.validators.type_id_validations import TypeIdValidations

logger = logging.getLogger('employee')

class EmployeeMenu:
    '''Performs all the employee related operations'''
    
    def __init__(self,user_id : str) -> None:
        '''Initialises user_id for a particular session, takes user id as parameter'''
        logging.info(LogStatements.employee_logged_in)
        print(StatementsConfig.welcome_employee)
        self.user_id = user_id

    def raise_issue(self) -> None:
        '''Method raises issues for maintenance'''
        issue_id = "ISN" + shortuuid.ShortUUID().random(length=4)
        result = db.display_data(
                    ConfigQueries.fetch_assigned_assets_by_uid,
                    ConfigQueries.schema_assets_to_user,
                    (self.user_id,)
                )
        if result == False:
            return
        asset_id = TypeIdValidations.input_asset_id()
        fetch_asset = db.fetch_data(
                        ConfigQueries.fetch_if_user_have_asset,
                        (asset_id,self.user_id)
                    )
        if not fetch_asset:
            print(StatementsConfig.assetid_not_exists)
            return     
        new_tuple = (issue_id,self.user_id,asset_id)
        db.save_data(
            ConfigQueries.insert_issue_for_asset,
            new_tuple
        )
        logging.info(LogStatements.issue_raised)
        print(StatementsConfig.issue_raised)

    def employee_operations(self) -> None: 
        '''Method of employee menu for operations'''   
        while True:       
            user_choice = int(input(PromptsConfig.employee_prompt))
            if user_choice == "1" : 
                result = db.display_data(
                            ConfigQueries.fetch_details_by_uid,
                            ConfigQueries.schema_user_table,
                            (self.user_id,)
                        )
                if result == False:
                        return
            elif user_choice == "2" :
                result = db.display_data(
                            ConfigQueries.fetch_assigned_assets_by_uid, 
                            ConfigQueries.schema_assets_to_user, 
                            (self.user_id,)
                        )
                if result == False:
                    return
            elif user_choice == "3" : 
                self.raise_issue()
            elif user_choice == "4" :
                return
            else :
                print(StatementsConfig.invalid_input) 
            if input("Press any key to continue....\n"):
                system('cls')
