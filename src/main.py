"""
    Module where the application starts, database connection in established, all tables are created if not exists
    loads all the configuration file and logger is initialised
"""
import logging
from models.database import db
from views.auth_views import AuthViews
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.DEBUG,
    filename=AppConfig.LOG_LOCATION,
)

logger = logging.getLogger("main")

if __name__ == "__main__":
    PromptConfig.load()
    LogsConfig.load()
    # creates all tables if not exists
    db.create_all_table()

    print(PromptConfig.STARTING_APPLICATION)
    logger.info(LogsConfig.LOG_STARTING_APPLICATION)

    # logins the user
    auth_obj = AuthViews()
    auth_obj.login()

    # closes database connection
    db.connection.close()
    print(PromptConfig.EXITING_APPLICATION)
    logger.info(LogsConfig.LOG_EXITING_APPLICATION)
