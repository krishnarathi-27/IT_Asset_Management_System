import shortuuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from models.database import db
from utils.mapped_roles import MappedRole
from controllers.asset_data_controllers import AssetDataControllers
from schemas.asset_schema import CategoryDetailsSchema, CategorySchema
from utils.rbac import role_required

blp = Blueprint("categories",__name__, description="Operations on asset category")

obj_asset_data_controller = AssetDataControllers(db)

@blp.route("/category")
class Categories(MethodView):
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.response(200,CategoryDetailsSchema(many=True))
    def get(self):
        data = obj_asset_data_controller.view_category()
        
        if not data:
            abort (404, message="Category data not exists")

        return data
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.arguments(CategorySchema)
    @blp.response(201,CategorySchema)
    def post(self, category_data):
        
        category_id = "CAT" + shortuuid.ShortUUID().random(length=4)

        result = obj_asset_data_controller.create_category(category_id,category_data['category_name'],
                                                            category_data['brand_name'],category_data['vendor_email'])
        
        if not result:
            abort (404, "Vendor do not exist in database")
        
        response = {
            "category_id": category_id,
            "category_name": category_data['category_name'],
            "brand_name": category_data['brand_name'],
            "vendor_email": category_data['vendor_email'],
            "message": "Category created successfully"
        }
        return response
       