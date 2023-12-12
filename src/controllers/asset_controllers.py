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
        return data
    
    def display_mapping_id(self) -> bool:
        data = db.fetch_data(
                    Queries.FETCH_MAPPING_ID
            )
        return data

    def add_asset_to_inventory(self,asset_type,mapping_id,purchased_date) -> bool:
        ''' Method to add assets in the inventory '''
        asset_id = "ASN" + shortuuid.ShortUUID().random(length=4)       
        data = db.fetch_data(
                Queries.FETCH_IF_MAPPING_ID_EXISTS,
                (mapping_id,)
            )
        if not data:
            return False  
        else:
            db.save_data(
                Queries.INSERY_ASSET_DETAILS,
                (asset_id,mapping_id,asset_type,purchased_date)
            )
            return True
    
    def view_assignable_asset(self):
        data_asset = db.fetch_data(
                        Queries.FETCH_ASSIGNABLE_ASSETS
                    )
        return data_asset
    
    def assign_asset(self,asset_id,user_id):
        """ Assign assets to the user that are vailable and assignable """
        data_asset_id = db.fetch_data(
                Queries.FETCH_IF_ASSET_EXISTS,
                (asset_id,)
            )
        if not data_asset_id:
            return False
               
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

    def view_unassignable_asset(self):
        data_asset = db.fetch_data(
                        Queries.FETCH_ASSIGNED_ASSETS_TO_UNASSIGN
                    )
        return data_asset
        
    def unassign_asset(self,asset_id):
        """ Unassign assets that are already assigned """
        data_asset_id = db.fetch_data(
                            Queries.FETCH_IF_ASSET_EXISTS,
                            (asset_id,)
                        )
        if not data_asset_id:
            return False
        else:
            db.save_data(
                Queries.UPDATE_ASSET_STATUS,
                (AppConfig.ASSET_LOCATION,AppConfig.AVAILABLE_STATUS,asset_id,)
            )
            return True