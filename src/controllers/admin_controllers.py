"""Module having buisness logic of admin functionalities"""
import logging
import hashlib
import shortuuid
from models.database import db
from config.queries import Queries
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger('admin_controller')

class AdminControllers:
    """
        Class containing methods to create new user and deactivate vendor
        ...
        Methods
        -------
        create_new_user() -> creates new user in the system
        deactivate_vendor() -> deactivate existing vendor in the system
    """

    def create_new_user(self,user_role: str,username,password) -> None:
        """
            Method for creating new user in the system with unique username
            Parameters : self, user_role, username, password
            Return Type : None
        """
        user_id = "EMP" + shortuuid.ShortUUID().random(length=4)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db.save_data(
            Queries.INSERT_USER_CREDENTIALS,
            (user_id,username,hashed_password,user_role,)
        )

        logger.info(LogsConfig.LOG_CREATE_NEW_USER)

    def deactivate_vendor(self,vendor_email) -> bool:
        """ Method for deactivating existing vendor in the system """
        
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
        