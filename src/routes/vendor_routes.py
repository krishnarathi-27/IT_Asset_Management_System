import shortuuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from controller.vendor_controller.create_vendor_controller import CreateVendorController
from controller.vendor_controller.view_vendor_controller import ViewVendorController
from controller.vendor_controller.delete_vendor_controller import DeleteVendorController
from utils.mapped_roles import MappedRole
from src.schemas.asset_schema import VendorSchema, VendorDetailsSchema, VendorDeactivateSchema
from utils.rbac import role_required

blp = Blueprint("vendors",__name__, description="Operations on asset vendors")
    
@blp.route("/vendors")
class Vendors(MethodView):

    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.response(200,VendorDetailsSchema(many=True))
    def get(self):
        
        obj_view_vendor = ViewVendorController()
        response = obj_view_vendor.view_all_vendor()

        return response
    
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
        
        obj_delete_vendor = DeleteVendorController()
        response = obj_delete_vendor.delete_vendor(vendor_id)

        return response
    