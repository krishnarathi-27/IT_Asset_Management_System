"""
    Module for validating user, changing their default passsword, and providing them role based access
"""
import hashlib
import logging
from models.database_helper import DatabaseHelper
from config.app_config import AppConfig
from utils.common_helper import CommonHelper
from config.log_prompts.logs_config import LogsConfig
from views.admin_views import AdminViews
from views.employee_views import EmployeeViews
from views.manager_views import ManagerViews

logger = logging.getLogger('auth_controller')

class AuthController:
    """
        Class containing methods for validating user, providing role based access and changing their default password.
        ...
        Attributes
        ----------
        db_obj -> object of DatabaseHelper class for accessing its methods.

        Methods
        -------
        first_login() -> private method, for checking if password entered matches with default password.
        role_based_access() -> private method, for providing role based access to the valid user
        validate_user() -> checks if the user entered credentials is a valid password or not 
    """
    def __init__(self) -> None:
        self.db_obj = DatabaseHelper()
        self.common_helper_obj = CommonHelper()

    def __first_login(self,username: str,hashed_input_password: str,password: str) -> bool:
        """
            Method for changing default password on first valid login
            Parameters : self, username, hashed_input_password, password
            Return type : bool
        """
        if hashed_input_password != password:
            logger.info("Wrong default password entered")
            return False
        else:
            logger.info("User changing default password")
            self.common_helper_obj.change_default_password(username)
            return True

    def __role_based_access(self,role: str,user_id: str) -> None:
        """
            Method for providig role based accessto valid user.
            Parameters : self, role, user_id
            Return type : None
        """
        logger.info(LogsConfig.PROVIDE_ROLE_BASED_ACCESS)
        
        if role == AppConfig.ADMININSTRATOR:
            admin_obj = AdminViews()     
            admin_obj.admin_operations()
        elif role == AppConfig.ASSET_MANAGER:
            manager_obj = ManagerViews(user_id)
            manager_obj.manager_operations()
        else:
            employee_obj = EmployeeViews(user_id)
            employee_obj.employee_operations()

    def validate_user(self,username: str,input_password: str) -> bool:
        """
            Method for validating user by their credentials
            Paramters : self, username, input_password
            Return type : bool
        """
        user_data = self.db_obj.get_user_credentials(username)
        if user_data:
            password = user_data[0][1]
            role = user_data[0][2]
            is_changed = user_data[0][3]
            user_id = user_data[0][0]
            hashed_password = hashlib.sha256(input_password.encode()).hexdigest()
            if is_changed == "false":
                logger.info("User logged in first time")
                return self.__first_login(username,hashed_password,password)
            else:             
                if hashed_password == password:
                    self.__role_based_access(role,user_id) 
                    return True
        return False
