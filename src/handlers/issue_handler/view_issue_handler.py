import shortuuid
import logging
from mysql.connector import Error, IntegrityError

from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import DataNotExists, DBException, DataAlreadyExists

logger = logging.getLogger('issue_handler')

class IssueHandler:

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def view_issues(self):
        try: 
            data = self.db_object.fetch_data(Queries.FETCH_ISSUE_TABLE)
            if data:
                return data
            else:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ISSUE_NOT_EXISTS)
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        
    def view_issue_by_userid(self,user_id):
        try: 
            data = self.db_object.fetch_data(Queries.FETCH_ISSUE_BY_USER_ID,(user_id,))
            if data:
                return data
            else:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ISSUE_NOT_EXISTS)
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        
    def create_issue(self,asset_id,user_id):
        try:
            asset_status = self.db_object.fetch_data(Queries.FETCH_IF_USER_HAVE_ASSET,(asset_id,user_id,))

            if not asset_status:
                 raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ASSET_ID_NOT_EXISTS)

            issue_id = PromptConfig.ISSUE_ID_PREFIX + shortuuid.ShortUUID().random(length=4)

            self.db_object.save_data(Queries.INSERT_ISSUE_FOR_ASSET,(issue_id,user_id,asset_id,))
            self.db_object.save_data(Queries.UPDATE_ASSET_STATUS_UNDER_MAINTENANCE,(asset_id,))

        except IntegrityError as err:
            logger.info(f"User with same username already exists {err}")
            raise DataAlreadyExists(409,PromptConfig.CONFLICT_MSG, PromptConfig.ISSUE_ALREADY_EXISTS)

        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500,PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        
    