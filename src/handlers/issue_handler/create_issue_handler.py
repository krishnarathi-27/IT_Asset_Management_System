import shortuuid
import pymysql
from flask import current_app as app

# local imports
from src.config.queries import Queries
from src.config.prompts.prompts import PromptConfig
from src.utils.exceptions import ApplicationException, DBException

class CreateIssueHandler:
    """Class having functionality to creaye new issue"""

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def create_issue(self,asset_id: str,user_id: str) -> str:
        """Method to create new issue for an employee with an asset id"""
        app.logger.info('Creating new issue for asset')

        try:
            asset_status = self.db_object.fetch_data(Queries.FETCH_IF_USER_HAVE_ASSET,(asset_id,user_id,))

            if not asset_status:
                 raise ApplicationException(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ASSET_ID_NOT_EXISTS)

            issue_id = PromptConfig.ISSUE_ID_PREFIX + shortuuid.ShortUUID().random(length=4)

            self.db_object.save_data(Queries.INSERT_ISSUE_FOR_ASSET,(issue_id,user_id,asset_id,))
            self.db_object.save_data(Queries.UPDATE_ASSET_STATUS_UNDER_MAINTENANCE,(asset_id,))

            app.logger.info(f'New issue created for {issue_id}')
            return issue_id

        except pymysql.IntegrityError as err:
            app.logger.info(f"User with same username already exists {err}")
            raise ApplicationException(409,PromptConfig.CONFLICT_MSG, PromptConfig.ISSUE_ALREADY_EXISTS)

        except pymysql.Error as err:
            app.logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500,PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)    
        