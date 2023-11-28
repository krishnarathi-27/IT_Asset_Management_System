import hashlib
import logging
import shortuuid
#local imports
from config.queries_config.queries_config import ConfigQueries
from config.prompts_config.prompts_config import PromptsConfig
from config.logs_config.log_statements import LogStatements
from database.database_helper import db
from config.statements.statements import StatementsConfig
from utils.validators.user_details_validations import UserDetailsValidations

logger = logging.getLogger('admin_actions')

class AdminActions:
    '''Class for Admin functionality to perform operation on user'''

    def select_user_role(self):
        while True:
            role = input(PromptsConfig.create_new_user_role) 
            if role == '1':
                user_role = StatementsConfig.asset_manager
                return user_role           
            elif role == '2':
                user_role = StatementsConfig.employee
                return user_role
            else:
                print(StatementsConfig.invalid_input)

    def create_new_user(self) -> None:
        '''Function that creates new user'''
        user_id = "EMP" + shortuuid.ShortUUID().random(length=4)
        while True:
            username = UserDetailsValidations.input_name()
            user_data = db.fetch_data(
                            ConfigQueries.fetch_user_credentials, 
                            (username,)
                        )
            if len(user_data) == 0:
                break
            print(StatementsConfig.username_exists)  
        user_role = self.select_user_role()      
        print(StatementsConfig.strong_password)
        password = UserDetailsValidations.input_password()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_tuple = (user_id,username,hashed_password,user_role)
        db.save_data(
            ConfigQueries.insert_user_credentials,
            user_tuple
        )
        print(StatementsConfig.user_added_success)
        logging.info(LogStatements.log_create_new_user)

    def delete_user(self) -> None:  
        '''Function that deletes new user'''
        username = UserDetailsValidations.input_name()
        user_data = db.fetch_data(
                        ConfigQueries.fetch_user_credentials, 
                        (username,)
                    )
        if len(user_data) == 0:
            print(StatementsConfig.user_not_exists)
            return False
        db.delete_data(
            ConfigQueries.delete_user_credentials,
            username
        )
        print(StatementsConfig.user_deleted_success)
        logging.info(LogStatements.log_delete_new_user)

    def view_user_details(self) -> None:   
        '''Function that view all the user'''
        result = db.display_data(
                    ConfigQueries.fetch_authentication_table,
                    ConfigQueries.schema_user_table
                )
        if result == False:
            return
        