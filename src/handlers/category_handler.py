import logging
import shortuuid
from mysql.connector import Error, IntegrityError

# local imports
from config.queries import Queries
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from utils.exceptions import DataAlreadyExists, DataNotExists, DBException

logger = logging.getLogger('category_handler')


class CategoryHandler:
    """
    Class containinig methods to create and view both category and vendor
    """
    def __init__(self, db_object) -> None:
        self.db_object = db_object
        
    def view_all_category(self) -> list:

        try:
            data = self.db_object.fetch_data(Queries.FETCH_CATEGORY_TABLE_WITH_VENDORS)

            if data:
                return data
            raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.CATEGORY_NOT_EXISTS)
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    
    def check_category_with_vendor(self, mapping_id: str, category_id: str, vendor_id: str) -> bool:

        mapping_data = self.db_object.fetch_data(
            Queries.FETCH_FROM_MAPPING_TABLE,
            (category_id,vendor_id,))

        if not mapping_data:
            self.db_object.save_data(
                Queries.INSERT_MAPPING_DETAILS,
                (mapping_id,category_id, vendor_id,))
            
            logging.info("New category created in database")
            return True

        else:
            raise IntegrityError

    def check_category(self, category_id,vendor_id: str, category_name: str, brand_name: str) -> bool:

        vendor_id = vendor_id[0][AppConfig.VENDOR_ID]
        
        category_exists = self.db_object.fetch_data(
            Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME,
            (category_name,brand_name,),
        )
        mapping_id = PromptConfig.MAPPING_ID_PREFIX + shortuuid.ShortUUID().random(length=4)

        if not category_exists:
            self.db_object.save_data(
                [Queries.INSERT_CATEGORY_DETAILS, Queries.INSERT_MAPPING_DETAILS],
                [(category_id, category_name,brand_name),
                 (mapping_id,category_id,vendor_id,)]
            )
            return True

        else:
            category_id = category_exists[0][AppConfig.CATEGORY_ID]
            return self.check_category_with_vendor(mapping_id, category_id, vendor_id)

    def create_category(self,category_name: str, brand_name: str, vendor_email: str) -> bool:

        try:
            vendor_id = self.db_object.fetch_data(Queries.FETCH_VENDOR_BY_EMAIL, (vendor_email,))

            if not vendor_id:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.VENDOR_NOT_EXISTS)

            else:
                category_id = PromptConfig.CATEGORY_ID_PREFIX + shortuuid.ShortUUID().random(length=4)
                category_name = category_name.lower()
                brand_name = brand_name.lower()
                return self.check_category(category_id, vendor_id, category_name, brand_name)
        
        except IntegrityError as err:
            logger.error(f'Same category name already exits {err}')
            raise DataAlreadyExists(409, PromptConfig.CONFLICT_MSG, PromptConfig.CATEGORY_ALREADY_EXISTS)
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        