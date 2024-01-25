from flask.views import MethodView
from flask_smorest import Blueprint

from controller.category_controller.view_category_controller import ViewCategoryController
from controller.category_controller.create_category_controller import CreateCategoryController
from utils.mapped_roles import MappedRole
from schemas.asset_schema import CategoryDetailsSchema, CategorySchema
from utils.rbac import role_required

blp = Blueprint("categories",__name__, description="Operations on asset category")

@blp.route("/categories")
class Categories(MethodView):
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.response(200,CategoryDetailsSchema(many=True))
    def get(self):

        obj_view_category = ViewCategoryController()
        response = obj_view_category.view_all_category()
        
        return response
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.arguments(CategorySchema)
    @blp.response(201,CategorySchema)
    def post(self, request_data):

        obj_create_category = CreateCategoryController()
        response = obj_create_category.create_new_category(request_data)

        return response
    
       