import shortuuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from controller.vendor.create_vendor import CreateVendorController
from utils.mapped_roles import MappedRole
from src.schemas.asset_schema import VendorSchema, VendorDetailsSchema, VendorDeactivateSchema
from utils.rbac import role_required

blp = Blueprint("vendors",__name__, description="Operations on asset vendors")
    
@blp.route("/vendor/all")
class Vendors(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.response(200,VendorDetailsSchema(many=True))
    def get(self):
        
        pass

@blp.route("/vendor")
class Vendor(MethodView):
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.arguments(VendorSchema)
    @blp.response(201,VendorSchema)
    def post(self, request_data):
        
        obj_create_vendor = CreateVendorController()
        response = obj_create_vendor.create_new_vendor(request_data)

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
    