"""Module contains methods which are sahred between admin and manager"""
import logging
import shortuuid

# local imports
from config.queries import Queries
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger("asset_data_controller")


class AssetDataControllers:
    """
    Class containinig methods to create and view both category and vendor
    """

    def __init__(self, db_object):
        self.db_object = db_object

    def check_category_with_vendor(self, mapping_id: str, category_id: str, vendor_id: str) -> bool:
        """
        Method that checks if category with same vendor exists or not
        Parameters : self, mapping_id, category_id, vendor_id
        Return type : bool
        """
        mapping_data = self.db_object.fetch_data(
            Queries.FETCH_FROM_MAPPING_TABLE,
            (
                category_id,
                vendor_id,
            ))

        if not mapping_data:
            self.db_object.save_data(
                Queries.INSERT_MAPPING_DETAILS,
                (
                    mapping_id,
                    category_id,
                    vendor_id,
                ))
            logging.info(LogsConfig.LOG_CATEGORY_ADDED)
            return True

        else:
            return False

    def check_category(self, category_id,vendor_id: str, category_name: str, brand_name: str) -> bool:
        """Method that checks if category exists or not"""

        vendor_id = vendor_id[0]['vendor_id']

        category_exists = self.db_object.fetch_data(
            Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME,
            (
                category_name,
                brand_name,
            ),
        )
        mapping_id = "MPN" + shortuuid.ShortUUID().random(length=4)

        if not category_exists:
            self.db_object.save_data(
                [Queries.INSERT_CATEGORY_DETAILS, Queries.INSERT_MAPPING_DETAILS],
                [
                    (
                        category_id,
                        category_name,
                        brand_name,
                    ),
                    (
                        mapping_id,
                        category_id,
                        vendor_id,
                    ),
                ]
            )
            return True

        else:
            category_id = category_exists[0][0]
            return self.check_category_with_vendor(mapping_id, category_id, vendor_id)

    def create_category(self,category_id, category_name: str, brand_name: str, vendor_email: str) -> bool:
        """Method that creates new category of asset"""

        vendor_id = self.db_object.fetch_data(Queries.FETCH_VENDOR_BY_EMAIL, (vendor_email,))
        print(vendor_id)
        if not vendor_id:
            return False

        else:
            return self.check_category(category_id, vendor_id, category_name, brand_name)

    def create_vendor(self,vendor_id, vendor_name: str, vendor_email: str) -> None:
        """Method that creates new vendor of asset"""
 
        result = self.db_object.save_data(
            Queries.INSERT_VENDOR_DETAILS,
            (
                vendor_id,
                vendor_name,
                vendor_email,
            )
        )
        logging.info(LogsConfig.LOG_VENDOR_ADDED)
        return result

    def view_vendor(self) -> list:
        """Method that views vendor details"""

        data = self.db_object.fetch_data(Queries.FETCH_VENDOR_TABLE)
        return data

    def view_category(self) -> list:
        """Method that views category details"""

        data = self.db_object.fetch_data(Queries.FETCH_CATEGORY_TABLE_WITH_VENDORS)
        return data

    def deactivate_vendor(self, vendor_id: str) -> bool:
        """Method for deactivating existing vendor in the system"""

        data = self.db_object.fetch_data(Queries.FETCH_VENDOR_BY_ID, (vendor_id,))

        if not data:
            return False

        result = self.db_object.save_data(Queries.UPDATE_VENDOR_ACTIVE_STATUS, (vendor_id,))
        logger.info(LogsConfig.LOG_VENDOR_DEACTIVATED)
        return True
    