import logging
import shortuuid

# local imports
from database.database import db as db_object
from config.queries import Queries
from config.log_prompts.logs_config import LogsConfig
from utils.exceptions import NoDataExistsException, VendorNotExistsException, CategoryAlreadyExistsException

logger = logging.getLogger("category_controller")


class CategoryHandler:
    """
    Class containinig methods to create and view both category and vendor
    """

    def view_all_category(self) -> list:

        data = db_object.fetch_data(Queries.FETCH_CATEGORY_TABLE_WITH_VENDORS)

        if data:
            return data
        raise NoDataExistsException
    
    def check_category_with_vendor(self, mapping_id: str, category_id: str, vendor_id: str) -> bool:

        mapping_data = db_object.fetch_data(
            Queries.FETCH_FROM_MAPPING_TABLE,
            (category_id,vendor_id,))

        if not mapping_data:
            db_object.save_data(
                Queries.INSERT_MAPPING_DETAILS,
                (mapping_id,category_id, vendor_id,))
            
            logging.info(LogsConfig.LOG_CATEGORY_ADDED)
            return True

        else:
            raise CategoryAlreadyExistsException

    def check_category(self, category_id,vendor_id: str, category_name: str, brand_name: str) -> bool:

        vendor_id = vendor_id[0]['vendor_id']

        category_exists = db_object.fetch_data(
            Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME,
            (category_name,brand_name,),
        )
        mapping_id = "MPN" + shortuuid.ShortUUID().random(length=4)

        if not category_exists:
            db_object.save_data(
                [Queries.INSERT_CATEGORY_DETAILS, Queries.INSERT_MAPPING_DETAILS],
                [(category_id, category_name,brand_name),
                 (mapping_id,category_id,vendor_id,)]
            )
            return True

        else:
            category_id = category_exists[0]['category_id']
            return self.check_category_with_vendor(mapping_id, category_id, vendor_id)

    def create_category(self,category_name: str, brand_name: str, vendor_email: str) -> bool:

        vendor_id = db_object.fetch_data(Queries.FETCH_VENDOR_BY_EMAIL, (vendor_email,))

        if not vendor_id:
            raise VendorNotExistsException

        else:
            category_id = "CAT" + shortuuid.ShortUUID().random(length=4)
            category_name = category_name.lower()
            brand_name = brand_name.lower()
            return self.check_category(category_id, vendor_id, category_name, brand_name)
    