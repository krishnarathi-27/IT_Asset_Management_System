import shortuuid
from models.database import db
from config.queries import Queries
from config.app_config import AppConfig
from config.queries import Header
from utils.common_helper import CommonHelper
from utils.validations import InputValidations

class AssetControllers:

    def view_asset(self) -> bool:
        data = data = db.fetch_data(
                Queries.FETCH_ASSETS_TABLE
            )
        if not data:
            return False
        CommonHelper.display_table(data,Header.SCHEMA_ASSET_TABLE)
        return True

    def add_asset_to_inventory(self,asset_type) -> bool:
        ''' Method to add assets in the inventory '''
        asset_id = "ASN" + shortuuid.ShortUUID().random(length=4)       
        data = db.fetch_data(
                    Queries.FETCH_MAPPING_ID
            )
        if not data:
            return False
        CommonHelper.display_table(data,Header.SCHEMA_MAPPING_CATGEORY_VENDOR_TABLE)

        mapping_id = InputValidations.input_mapping_id()
        data = db.fetch_data(
                Queries.FETCH_IF_MAPPING_ID_EXISTS,
                (mapping_id,)
            )
        if not data:
            return False
        
        purchased_date = InputValidations.input_date()    
        db.save_data(
            Queries.INSERY_ASSET_DETAILS,
            (asset_id,mapping_id,asset_type,purchased_date)
        )
        return True
    
    def assign_asset(self):
        data_asset = db.fetch_data(
                        Queries.FETCH_ASSIGNABLE_ASSETS
                    )
        if not data_asset:
            return False
        
        CommonHelper.display_table(data_asset,Header.SCHEMA_ASSIGNABLE_ASSET_DETAILS)
        asset_id = InputValidations.input_asset_id()
        data_asset_id = db.fetch_data(
                Queries.FETCH_IF_ASSET_EXISTS,
                (asset_id,)
            )
        if not data_asset_id:
            return False
        
        data_user = db.fetch_data(
                        Queries.FETCH_AUTHENTICATION_TABLE
                )
        if not data_user:
            return False
        
        CommonHelper.display_table(data_user,Header.SCHEMA_USER_TABLE)
        user_id = InputValidations.input_user_id()
        data_user_id = db.fetch_data(
                Queries.FETCH_IF_USER_EXISTS,
                (user_id,)
            )
        if not data_user_id:
            return False
        
        db.save_data(
            Queries.UPDATE_ASSET_STATUS,
            (user_id,AppConfig.UNAVAILABLE_STATUS,asset_id,)
        )
        return True
    
    def unassign_asset(self):
        data_asset = db.fetch_data(
                    Queries.FETCH_ASSIGNED_ASSETS_TO_UNASSIGN
                )
        if not data_asset:
            return False
        
        CommonHelper.display_table(data_asset,Header.SCHEMA_ASSET_TABLE)
        asset_id = InputValidations.input_asset_id()
        data_asset_id = db.fetch_data(
                            Queries.FETCH_IF_ASSET_EXISTS,
                            (asset_id,)
                        )
        if not data_asset_id:
            return False
        
        db.save_data(
            Queries.UPDATE_ASSET_STATUS,
            (AppConfig.ASSET_LOCATION,AppConfig.AVAILABLE_STATUS,asset_id,)
        )
        return True