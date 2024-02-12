from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from utils.mapped_roles import MappedRole
from config.app_config import AppConfig
from utils.rbac import role_required
from controller.asset_controller.create_asset_controller import CreateAssetController
from controller.asset_controller.view_asset_controller import ViewAssetController
from controller.asset_controller.update_asset_controller import UpdateAssetController
from schemas.asset_schema import AssetSchema, ViewAssetSchema, AssetUpdateSchema

blp = Blueprint("assets",__name__, description="Operations on asset inventory")

@blp.route("/assets")
class Assets(MethodView):
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.response(200,ViewAssetSchema(many=True))
    def get(self):

        obj_view_asset = ViewAssetController()
        response = obj_view_asset.view_all_asset()
            
        return response
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @role_required([MappedRole.MANAGER_ROLE])
    @blp.arguments(AssetSchema)
    @blp.response(201,AssetSchema)
    def post(self,request_data):

        obj_create_asset= CreateAssetController()
        response = obj_create_asset.create_asset(request_data)

        return response
    
@blp.route("/assets/<string:asset_id>/assign")
class AssetAssign(MethodView):
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @role_required([MappedRole.MANAGER_ROLE])
    @blp.arguments(AssetUpdateSchema)
    @blp.response(200,AssetUpdateSchema)
    def put(self,request_data,asset_id):

        obj_update_user = UpdateAssetController()
        response = obj_update_user.assign_asset(request_data,asset_id)

        return response

@blp.route("/assets/<string:asset_id>/unassign")
class AssetUnassign(MethodView):
     
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @role_required([MappedRole.MANAGER_ROLE])
    @blp.arguments(AssetUpdateSchema)
    @blp.response(200,AssetUpdateSchema)
    def put(self,request_data,asset_id):

        obj_update_user = UpdateAssetController()
        response = obj_update_user.unassign_asset(request_data, asset_id)

        return response
    