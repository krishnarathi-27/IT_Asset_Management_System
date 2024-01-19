"""Module having buisness logic of admin functionalities"""
import logging
import hashlib
import shortuuid

# local imports
from config.queries import Queries
from config.log_prompts.logs_config import LogsConfig
from models.database import db

logger = logging.getLogger("admin_controller")


class AdminControllers:
    """
    Class containing methods to create new user and deactivate vendor
    """

    def create_new_user(self, user_role: str, username: str, password: str) -> None:
        """
        Method for creating new user in the system with unique username
        Parameters : self, user_role, username, password
        Return Type : None
        """
        user_id = "EMP" + shortuuid.ShortUUID().random(length=4)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db.save_data(
            Queries.INSERT_USER_CREDENTIALS,
            (
                user_id,
                username,
                hashed_password,
                user_role,
            ),
        )

    def deactivate_vendor(self, vendor_email: str) -> bool:
        """Method for deactivating existing vendor in the system"""

        data = db.fetch_data(Queries.FETCH_VENDOR_BY_EMAIL, (vendor_email,))

        if not data:
            return False

        db.save_data(Queries.UPDATE_VENDOR_ACTIVE_STATUS, (vendor_email,))
        logger.info(LogsConfig.LOG_VENDOR_DEACTIVATED)
        return True
