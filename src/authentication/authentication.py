import hashlib
import logging
import time
from pwinput import pwinput
#local imports
from admin.admin_menu import AdminMenu
from config.statements.statements import StatementsConfig
from config.queries_config.queries_config import ConfigQueries
from config.logs_config.log_statements import LogStatements
from database.database_helper import db
from employee.employee_menu import EmployeeMenu
from manager.manager_menu import ManagerMenu
from utils.validators.user_details_validations import UserDetailsValidations

logger = logging.getLogger('authentication')

class Authentication:
    '''Class authenticates existing user and gives role based access'''
  
    def __init__(self) -> None:
        '''sets the maximum login attempts'''
        self.login_attempts = StatementsConfig.max_login_attempts

    def invalid_login(self) -> None:
        '''decreases the login attempts on each invalid login'''
        self.login_attempts -= 1
        logger.debug(LogStatements.invalid_login_log)
        print(StatementsConfig.invalid_login.format(self.login_attempts))
    
    def change_default_password(self,username: str,password: str) -> None:
        '''changes default password assigned by admin'''
        default_password = pwinput(prompt=StatementsConfig.input_default_password)
        hashed_password = hashlib.sha256(default_password.encode()).hexdigest()
        if password != hashed_password:
            self.invalid_login()
        else:
            while True:
                print(StatementsConfig.strong_password)
                new_password = UserDetailsValidations.input_password()
                print(StatementsConfig.input_confirm_password)
                confirm_password = UserDetailsValidations.input_password()
                if new_password != confirm_password:
                    print(StatementsConfig.password_not_match)
                else:
                    new_hashed_password = hashlib.sha256(new_password.encode()).hexdigest()    
                    new_tuple = (new_hashed_password,username)
                    db.save_data(ConfigQueries.update_default_password, new_tuple)
                    print(StatementsConfig.default_password_updated)
                    logging.info(LogStatements.default_pwd_updated_log)
                    break

    def role_based_access(self,role: str,user_id: str) -> None:
        '''provides role based access to the user'''
        logging.info(StatementsConfig.provide_role_based_access)
        if role == StatementsConfig.administrator:
            admin_obj = AdminMenu()     
            admin_obj.admin_operations()
        elif role == StatementsConfig.asset_manager:
            manager_obj = ManagerMenu(user_id)
            manager_obj.manager_operations()
        else:
            employee_obj = EmployeeMenu(user_id)
            employee_obj.employee_operations()
        choice = input(StatementsConfig.login_again).lower().strip()
        if choice == 'n':
            exit()
        elif choice == 'y':
            self.login_attempts = 3
            return
        else :
            print(StatementsConfig.invalid_input)

    def login(self) -> None:
        '''authenticates the valid user'''
        print(StatementsConfig.attempts_message)
        while True:
            if self.login_attempts == 0:
                print(StatementsConfig.attempts_exhausted)
                logging.debug(StatementsConfig.attempts_exhausted)
                self.login_attempts = 3
                print(StatementsConfig.wait_for_login)
                time.sleep(20)        
            else:
                username = input(StatementsConfig.enter_username)
                user_data = db.fetch_data(
                                ConfigQueries.fetch_user_credentials,
                                (username, )
                            )
                if not user_data:
                    self.invalid_login()
                else:
                    password = user_data[0][1]
                    role = user_data[0][2]
                    is_changed = user_data[0][3]
                    user_id = user_data[0][0]
                    if is_changed == "false":
                        self.change_default_password(username,password)
                    else:
                        input_password = pwinput(StatementsConfig.enter_password)
                        hashed_password = hashlib.sha256(input_password.encode()).hexdigest()
                        if hashed_password != password:
                            self.invalid_login()
                        else:
                            self.role_based_access(role,user_id)  
                                                                   