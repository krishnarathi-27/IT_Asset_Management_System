import shortuuid
from config.app_config import AppConfig
from config.queries import Header
from models.database_helper import DatabaseHelper
from utils.common_helper import CommonHelper
from utils.validations import InputValidations

class AssetControllers:

    def __init__(self) -> None:
        self.obj_db_helper = DatabaseHelper()
        self.obj_common_helper = CommonHelper()

    def view_asset(self) -> bool:
        data = self.obj_db_helper.get_asset_details()
        if not data:
            return False
        CommonHelper.display_table(data,Header.SCHEMA_ASSET_TABLE)
        return True

    def add_asset_to_inventory(self,asset_type) -> bool:
        '''
            Method to add assets in the inventory
            Parameters : self
            Return type : bool
        '''
        asset_id = "ASN" + shortuuid.ShortUUID().random(length=4)       
        data = self.obj_db_helper.get_category_vendor_details()
        if not data:
            return False
        CommonHelper.display_table(data,Header.SCHEMA_MAPPING_CATGEORY_VENDOR_TABLE)

        mapping_id = InputValidations.input_mapping_id()
        data = self.obj_db_helper.get_data_if_mapping_id(mapping_id)
        if not data:
            return False
        purchased_date = InputValidations.input_date()    
        self.obj_db_helper.save_asset_details(asset_id,mapping_id,asset_type,purchased_date)
        return True
    
    def assign_asset(self):
        data_asset = self.obj_db_helper.fetch_assignable_asset()
        if not data_asset:
            return False
        
        CommonHelper.display_table(data_asset,Header.SCHEMA_ASSIGNABLE_ASSET_DETAILS)
        asset_id = InputValidations.input_asset_id()
        data_asset_id = self.obj_db_helper.fetch_asset_exists(asset_id)
        if not data_asset_id:
            return False
        
        data_user = self.obj_db_helper.get_user_details()
        if not data_user:
            return False
        
        CommonHelper.display_table(data_user,Header.SCHEMA_USER_TABLE)
        user_id = InputValidations.input_user_id()
        data_user_id = self.obj_db_helper.fetch_user_exists(user_id)
        if not data_user_id:
            return False
        
        self.obj_db_helper.save_asset_status(user_id,AppConfig.UNAVAILABLE_STATUS,asset_id)
        return True
    
    def unassign_asset(self):
        data_asset = self.obj_db_helper.fetch_unassignable_assets()
        if not data_asset:
            return False
        
        CommonHelper.display_table(data_asset,Header.SCHEMA_ASSET_TABLE)
        asset_id = InputValidations.input_asset_id()
        data_asset_id = self.obj_db_helper.fetch_asset_exists(asset_id)
        if not data_asset_id:
            return False
        
        self.obj_db_helper.save_asset_status(AppConfig.ASSET_LOCATION,AppConfig.AVAILABLE_STATUS,asset_id)
        return True