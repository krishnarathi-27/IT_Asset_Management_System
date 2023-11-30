import shortuuid
from config.queries import Header
from models.database_helper import DatabaseHelper
from utils.common_helper import CommonHelper
from utils.validations import InputValidations

class AssetControllers:

    def __init__(self) -> None:
        self.db_obj = DatabaseHelper()
        self.common_helper_obj = CommonHelper()

    def add_asset_to_inventory(self,asset_type) -> bool:
        '''
            Method to add assets in the inventory
            Parameters : self
            Return type : bool
        '''
        asset_id = "ASN" + shortuuid.ShortUUID().random(length=4)       
        data = self.db_obj.get_category_vendor_details()
        if not data:
            return False
        CommonHelper.display_table(data,Header.SCHEMA_MAPPING_CATGEORY_VENDOR_TABLE)

        mapping_id = InputValidations.input_mapping_id()
        data = self.db_obj.get_data_if_mapping_id(mapping_id)
        if not data:
            return False
        purchased_date = InputValidations.input_date()    
        self.db_obj.save_asset_details(asset_id,mapping_id,asset_type,purchased_date)
