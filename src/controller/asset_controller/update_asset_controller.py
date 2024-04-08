from flask import current_app as app

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.asset_handler.update_asset_handler import UpdateAssetHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.response import SuccessResponse, ErrorResponse

class UpdateAssetController:
    """Controller to update assets status"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_asset_handler = UpdateAssetHandler(db_object)

    def assign_asset(self, request_data: dict, asset_id: str) -> dict:
        """Function to assign asset to user"""
        app.logger.info("Assigning assets to user")

        try:
            assigned_to= request_data['assigned_to']
            
            self.obj_asset_handler.assign_asset(asset_id, assigned_to)

            app.logger.info(f'Assets assigned to user {assigned_to}')
            return SuccessResponse.success_message(PromptConfig.ASSET_ASSIGNED), StatusCodes.OK
        
        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
    def unassign_asset(self, request_data: dict, asset_id: str) -> dict:
        """Function to unassign assigned asset from user"""
        app.logger.info('Asset unassigned successfully')

        try:

            self.obj_asset_handler.unassign_asset(asset_id)

            return SuccessResponse.success_message(PromptConfig.ASSET_UNASSIGNED), StatusCodes.OK
        
        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        