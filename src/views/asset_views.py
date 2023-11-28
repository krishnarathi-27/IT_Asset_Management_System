import logging
from utils.common_helper import CommonHelper
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger('auth_views')

class ManagerViews:
    """
        Class that contains methos to perform operations on assets
        ...
        Attributes
        ----------
        obj_common_helper = object of class CommonHelper
        Methods
        -------

    """
    def __init__(self) -> None:
        logger.info(LogsConfig.LOG_MANAGER_LOGGED_IN)
        print(PromptConfig.WELCOME_MANAGER)
        self.obj_common_helper = CommonHelper()