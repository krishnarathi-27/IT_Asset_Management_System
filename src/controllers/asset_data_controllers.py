"""Module contains methods which are sahred between admin and manager"""
import logging
import shortuuid
from models.database import db
from config.queries import Queries
from config.queries import Header
from utils.common_helper import CommonHelper
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger('asset_data_controller')

class AssetDataControllers:
    """
        Class containinig methods to create and view both category and vendor
        ...
        Attributes
        ----------
        db_obj -> object of DatabaseHelper class for accessing its methods.
        Methods
        -------
        category_vendor_exists() -> checks if category with same vendor exists or not
        create_category() -> creates new category of asset
        create_vendor() -> creates new vendor 
        view_vendor() -> view vendor details
        view_category() -> view category details
    """
    def category_vendor_exists(self,mapping_id: str, category_id: str, vendor_id: str) -> bool:
        """
            Method that checks if category with same vendor exists or not 
            Parameters : self, mapping_id, category_id, vendor_id
            Return type : bool
        """
        mapping_data = db.fetch_data(
                            Queries.FETCH_FROM_MAPPING_TABLE,
                            (category_id,vendor_id,)
                        )
        if not mapping_data:
            db.save_data(
                Queries.INSERT_MAPPING_DETAILS,
                (mapping_id,category_id,vendor_id,)
            )
            logging.info(LogsConfig.LOG_CATEGORY_ADDED)
            return True
        else:
            return False

    def create_category(self) -> bool:
        """
            Method that creates new category of asset
            Parameters : self
            Return type : bool
        """
        data = CommonHelper.input_category_details()
        category_id = "CAT" + shortuuid.ShortUUID().random(length=4) 
        vendor_id = db.fetch_data(
                        Queries.FETCH_VENDOR_BY_EMAIL,
                        (data[2],)
                    )
        if not vendor_id:
            return False
        vendor_id = vendor_id[0][0]
        category_exists = db.fetch_data(
                        Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME,
                        (data[0],data[1],)
                    )
        mapping_id = "MPN" + shortuuid.ShortUUID().random(length=4)
        if not category_exists:
            db.save_data([
                    Queries.INSERT_CATEGORY_DETAILS,
                    Queries.INSERT_MAPPING_DETAILS
                ],
                [(category_id,data[0],data[1],),
                (mapping_id,category_id,vendor_id,)
            ])
            return True
        else:
            category_id = category_exists[0][0]
            return self.category_vendor_exists(mapping_id,category_id,vendor_id)

    def create_vendor(self,vendor_email,vendor_name) -> None:
        """
            Method that creates new vendor of asset
            Parameters : self
            Return type : None
        """
        vendor_id = "VEN" + shortuuid.ShortUUID().random(length=4)         
        db.save_data(
            Queries.INSERT_VENDOR_DETAILS,
            (vendor_id,vendor_name,vendor_email,)
        )
        logging.info(LogsConfig.LOG_VENDOR_ADDED)

    def view_vendor(self) -> bool:
        """
            Method that views vendor details
            Parameters : self
            Return type : bool
        """
        data = db.fetch_data(
                    Queries.FETCH_VENDOR_TABLE
                )
        if not data:
            return False
        CommonHelper.display_table(data,Header.SCHEMA_VENDOR_TABLE)
        return True

    def view_category(self) -> bool:
        """
            Method that views category details
            Parameters : self
            Return type : bool
        """
        data = db.fetch_data(
                    Queries.FETCH_CATEGORY_TABLE
                )
        if not data:
            return False
        CommonHelper.display_table(data,Header.SCHEMA_CATEGORY_TABLE)
        return True
    