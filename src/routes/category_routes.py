from flask.views import MethodView
from flask_smorest import Blueprint

from src.config.app_config import AppConfig
from src.controller.category_controller.view_category_controller import ViewCategoryController
from src.controller.category_controller.create_category_controller import CreateCategoryController
from src.schemas.asset_schema import CategoryDetailsSchema, CategorySchema
from src.utils.rbac import access_required, ROLE_REQUIRED

blp = Blueprint("categories",__name__, description="Operations on asset category")

@blp.route("/v1/categories")
class Categories(MethodView):
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @access_required([ROLE_REQUIRED['admin'],ROLE_REQUIRED['asset manager']])
    @blp.response(200,CategoryDetailsSchema(many=True))
    def get(self):

        obj_view_category = ViewCategoryController()
        response = obj_view_category.view_all_category()
        
        return response
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @access_required([ROLE_REQUIRED['admin'],ROLE_REQUIRED['asset manager']])
    @blp.arguments(CategorySchema)
    @blp.response(201,CategorySchema)
    def post(self, request_data):

        obj_create_category = CreateCategoryController()
        response = obj_create_category.create_new_category(request_data)

        return response
       