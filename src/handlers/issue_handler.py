import shortuuid
import logging
from mysql.connector import Error, IntegrityError

from database.database import db as db_object
from config.queries import Queries
from utils.exceptions import DataNotExists, DBException, DataAlreadyExists

logger = logging.getLogger('issue_handler')

class IssueHandler:

    def view_issues(self):
        try: 
            data = db_object.fetch_data(Queries.FETCH_ISSUE_TABLE)
            if data:
                return data
            else:
                raise DataNotExists(404, 'Resource not found', 'No issues available')
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
        
    def view_issue_by_userid(self,user_id):
        try: 
            data = db_object.fetch_data(Queries.FETCH_ISSUE_BY_USER_ID,(user_id,))
            if data:
                return data
            else:
                raise DataNotExists(404, 'Resource not found', 'No issues available')
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
        
    def create_issue(self,asset_id,user_id):
        try:
            asset_status = db_object.fetch_data(Queries.FETCH_IF_USER_HAVE_ASSET,(asset_id,user_id,))

            if not asset_status:
                 raise DataNotExists(404, 'Resource not found', 'Asset id not available for user')

            issue_id = "ISN" + shortuuid.ShortUUID().random(length=4)

            db_object.save_data(Queries.INSERT_ISSUE_FOR_ASSET,(issue_id,user_id,asset_id,))
            db_object.save_data(Queries.UPDATE_ASSET_STATUS_UNDER_MAINTENANCE,(asset_id,))

        except IntegrityError as err:
            logger.info(f"User with same username already exists {err}")
            raise DataAlreadyExists(409, 'conflict', 'Username already exists')

        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
        
    