import logging
import shortuuid
from datetime import datetime
from os import system
#local imports
from config.queries_config.queries_config import ConfigQueries
from config.prompts_config.prompts_config import PromptsConfig
from config.statements.statements import StatementsConfig
from database.database_helper import db
from utils.validators.type_id_validations import TypeIdValidations

logger = logging.getLogger('maintenance')

class Maintenance:
    '''Class to handle maintenance related operation'''

    def __init__(self,user_id: str) -> None:
        '''Method to initialise manager id for the session'''
        self.user_id = user_id

    def view_pending_issues(self) -> None:
        '''Method to view pending issues'''
        result = db.display_data(
                    ConfigQueries.fetch_issues_pending,
                    ConfigQueries.schema_pending_issues
                )
        if result == False:
            return

    def send_asset(self) -> None:
        '''Method to send asset for maintenance'''
        self.view_pending_issues()
        print(StatementsConfig.select_from_table)
        issue_id = TypeIdValidations.input_issue_id()
        asset_id = db.fetch_data(
                        ConfigQueries.fetch_asset_id_by_issue_id,
                        (issue_id,)
                    )
        if not asset_id:
            return
        asset_id = asset_id[0][0]
        maintenance_id = "MTN" + shortuuid.ShortUUID().random(length=4)
        dt = datetime.now()
        start_date = dt.strftime(StatementsConfig.date_format)
        db.save_data(
            ConfigQueries.update_issue_status_under_maintenance, 
            (self.user_id,issue_id,)
        )
        db.save_data(
            ConfigQueries.insert_in_maintenance_table,
            (maintenance_id,asset_id,start_date,)
        )
        db.save_data(
            ConfigQueries.update_asset_status_under_maintenance,
            (asset_id,)
        )
        print(StatementsConfig.send_for_maintenance)

    def recieve_asset(self) -> None:
        '''Method to recieve asset from maintenance'''
        result = db.display_data(
                    ConfigQueries.fetch_maintenance_table,
                    ConfigQueries.schema_maintenance_table
                )     
        if result == False:
            return
        print(StatementsConfig.select_from_table)
        maintenance_id = TypeIdValidations.input_maintenance_id()
        asset_id = db.fetch_data(
                        ConfigQueries.fetch_asset_id_by_maintenance_table,
                        (maintenance_id,)
                    )   
        if not asset_id:
            return
        asset_id = asset_id[0][0]
        dt = datetime.now()
        return_date = dt.strftime(StatementsConfig.date_format)
        db.save_data(
            ConfigQueries.update_maintenance_return_date,
            (return_date,maintenance_id,)
        )
        db.save_data(
            ConfigQueries.update_asset_status_again_to_available,
            (asset_id,)
        )
        print(StatementsConfig.recieve_from_maintenance)

    def menu_operation(self) -> None:
        '''Method for menu operation in maintenance related task'''
        while True:
            user_choice = input(PromptsConfig.maintenance_prompt)
            if user_choice == "1" :
                self.view_pending_issues()
            elif user_choice == "2" :
                self.send_asset()
            elif user_choice == "3" :
                self.recieve_asset()
            elif user_choice == "4" :
                return
            else:
                print(StatementsConfig.invalid_input)
            if input("Press any key to continue....\n"):
                system('cls')
                