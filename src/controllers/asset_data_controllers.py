"""Module contains methods which are sahred between admin and manager"""
import logging
import shortuuid
from config.queries import Header
from utils.common_helper import CommonHelper
from utils.validations import InputValidations
from models.database_helper import DatabaseHelper
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
    def __init__(self) -> None:
        self.obj_db_helper = DatabaseHelper()

    def category_vendor_exists(self,mapping_id: str, category_id: str, vendor_id: str) -> bool:
        """
            Method that checks if category with same vendor exists or not 
            Parameters : self, mapping_id, category_id, vendor_id
            Return type : bool
        """
        mapping_data = self.obj_db_helper.get_from_mapping_table(category_id, vendor_id)
        if not mapping_data:
            self.obj_db_helper.save_data_in_mapping_table(mapping_id,category_id,vendor_id)
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
        vendor_id = self.obj_db_helper.get_vendor_by_email(data[2])
        if not vendor_id:
            return False
        vendor_id = vendor_id[0][0]
        category_exists = self.obj_db_helper.get_by_category_and_brand_name(data[0],data[1])
        mapping_id = "MPN" + shortuuid.ShortUUID().random(length=4)
        if not category_exists:
            self.obj_db_helper.save_category_mapping_details(
                (category_id,data[0],data[1]),
                (mapping_id,category_id,vendor_id)
            )
            return True
        else:
            category_id = category_exists[0][0]
            return self.category_vendor_exists(mapping_id,category_id,vendor_id)

    def create_vendor(self) -> None:
        """
            Method that creates new vendor of asset
            Parameters : self
            Return type : bool
        """
        vendor_id = "VEN" + shortuuid.ShortUUID().random(length=4)         
        vendor_email = InputValidations.input_email()
        vendor_name = InputValidations.input_name()
        self.obj_db_helper.save_new_vendor(vendor_id,vendor_name,vendor_email)
        logging.info(LogsConfig.LOG_VENDOR_ADDED)

    def view_vendor(self) -> bool:
        """
            Method that views vendor details
            Parameters : self
            Return type : bool
        """
        data = self.obj_db_helper.get_vendor_details()
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
        data = self.obj_db_helper.get_category_details()
        if not data:
            return False
        CommonHelper.display_table(data,Header.SCHEMA_CATEGORY_TABLE)
        return True
    