"""Module having buisness logic of admin functionalities"""
import logging
import hashlib
import shortuuid
from models.database import db
from config.queries import Queries
from config.queries import Header
from utils.validations import InputValidations
from config.log_prompts.logs_config import LogsConfig
from utils.common_helper import CommonHelper

logger = logging.getLogger('admin_controller')

class AdminControllers:
    """
        Class containing methods to create new user and deactivate vendor
        ...
        Attributes 
        ----------
        obj_db_helper -> object of DatabaseHelper class for accessing its methods
        Methods
        -------
        create_new_user() -> creates new user in the system
        deactivate_vendor() -> deactivate existing vendor in the system
    """

    def create_new_user(self,user_role: str) -> None:
        """
            Method for creating new user in the system with unique username
            Parameters : self, user_role
            Return Type : None
        """
        user_id = "EMP" + shortuuid.ShortUUID().random(length=4)
        username = InputValidations.input_name() 
        password =  InputValidations.input_password()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db.save_data(
            Queries.INSERT_USER_CREDENTIALS,
            (user_id,username,hashed_password,user_role,)
        )

        logger.info(LogsConfig.LOG_CREATE_NEW_USER)

    def deactivate_vendor(self) -> bool:
        """
            Method for deactivating existing vendor in the system
            Parameters : self
            Return Type : bool
        """
        data = db.fetch_data(
                    Queries.FETCH_VENDOR_TABLE
                )
        if not data:
            return False
        CommonHelper.display_table(data,Header.SCHEMA_VENDOR_TABLE)
        vendor_email = InputValidations.input_email()
        data = db.fetch_data(
                    Queries.FETCH_VENDOR_BY_EMAIL,
                    (vendor_email,)
                )
        if not data:
            return False
        db.save_data(
            Queries.UPDATE_VENDOR_ACTIVE_STATUS,
            (vendor_email,)
        )
        logger.info(LogsConfig.LOG_VENDOR_DEACTIVATED)
        return True
        
