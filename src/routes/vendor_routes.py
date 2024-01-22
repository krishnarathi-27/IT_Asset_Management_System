import shortuuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from models.database import db
from utils.mapped_roles import MappedRole
from controllers.asset_data_controllers import AssetDataControllers
from src.schemas.asset_schema import VendorSchema, VendorDetailsSchema, VendorDeactivateSchema
from utils.rbac import role_required

blp = Blueprint("vendors",__name__, description="Operations on asset vendors")

obj_asset_data_controller = AssetDataControllers(db)
    
@blp.route("/vendor")
class Vendors(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.response(200,VendorDetailsSchema(many=True))
    def get(self):
        data = obj_asset_data_controller.view_vendor()

        if not data:
            abort (404, message="Vendor data not exists")
        
        return data
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.arguments(VendorSchema)
    @blp.response(201,VendorSchema)
    def post(self, vendor_data):
        vendor_id = "VEN" + shortuuid.ShortUUID().random(length=4)

        obj_asset_data_controller.create_vendor(vendor_id,vendor_data['vendor_name'],vendor_data['vendor_email'])

        response = {
            "vendor_id": vendor_id,
            "vendor_name": vendor_data['vendor_name'],
            "vendor_email": vendor_data['vendor_email'],
            "message": "Vendor created successfully"
        }

        return response
    
@blp.route("/vendor/<string:vendor_id>")
class Vendor(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @blp.response(200,VendorDeactivateSchema)
    def delete(self, vendor_id):
        
        result = obj_asset_data_controller.deactivate_vendor(vendor_id)
        
        if not result:
            abort (404, message="Vendor not exists")

        return {"message": "Vendor deactivated successfully"}, 200
    