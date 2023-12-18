""" Module that controls the buisness logic of assets with database"""
import logging
import shortuuid

# local imports
from models.database import db
from config.queries import Queries
from config.app_config import AppConfig
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger("asset_controllers")

class AssetControllers:
    """
    Class containing methods to fetch assets from database and perform CRUD on assets in the inventory
    """

    def view_asset(self) -> list:
        """Methods that fetch asset from inventory"""

        data = data = db.fetch_data(Queries.FETCH_ASSETS_TABLE)
        return data

    def display_mapping_id(self) -> list:
        """Methods that fetch mapping id from database"""

        data = db.fetch_data(Queries.FETCH_MAPPING_ID)
        return data

    def add_asset_to_inventory(
        self, asset_type: str, mapping_id: str, purchased_date: str
    ) -> bool:
        """Method to add assets in the inventory"""

        asset_id = "ASN" + shortuuid.ShortUUID().random(length=4)
        data = db.fetch_data(Queries.FETCH_IF_MAPPING_ID_EXISTS, (mapping_id,))

        if not data:
            return False

        else:
            db.save_data(
                Queries.INSERY_ASSET_DETAILS,
                (asset_id, mapping_id, asset_type, purchased_date),
            )
            logger.info(LogsConfig.LOG_ASSET_ADDED_INVENTORY)
            return True

    def view_assignable_asset(self) -> list:
        """Method that fetch assignable asset from database"""

        data_asset = db.fetch_data(Queries.FETCH_ASSIGNABLE_ASSETS)
        return data_asset

    def assign_asset(self, asset_id: str, user_id: str) -> bool:
        """Assign assets to the user that are available and assignable"""

        data_asset_id = db.fetch_data(Queries.FETCH_IF_ASSET_EXISTS, (asset_id,))

        if not data_asset_id:
            return False

        data_user_id = db.fetch_data(Queries.FETCH_IF_USER_EXISTS, (user_id,))

        if not data_user_id:
            return False

        db.save_data(
            Queries.UPDATE_ASSET_STATUS,
            (
                user_id,
                AppConfig.UNAVAILABLE_STATUS,
                asset_id,
            ),
        )
        return True

    def view_unassignable_asset(self) -> list:
        """Methods that fetch unassignable asset from database"""

        data_asset = db.fetch_data(Queries.FETCH_ASSIGNED_ASSETS_TO_UNASSIGN)
        return data_asset

    def unassign_asset(self, asset_id: str) -> bool:
        """Unassign assets that are already assigned"""

        data_asset_id = db.fetch_data(Queries.FETCH_IF_ASSET_EXISTS, (asset_id,))

        if not data_asset_id:
            return False

        else:
            db.save_data(
                Queries.UPDATE_ASSET_STATUS,
                (
                    AppConfig.ASSET_LOCATION,
                    AppConfig.AVAILABLE_STATUS,
                    asset_id,
                ),
            )
            return True
