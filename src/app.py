import logging
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from datetime import timedelta

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db

from routes.auth_routes import blp as AuthRoutes
from routes.user_routes import blp as UserRoutes
from src.routes.category_routes import blp as CategoryRoutes
from src.routes.vendor_routes import blp as VendorRoutes
from src.routes.asset_routes import blp as AssetRoutes
from src.routes.issue_routes import blp as IssueRoutes

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.DEBUG,
    filename=AppConfig.LOG_LOCATION,
)

logger = logging.getLogger("main")

def create_app():

    PromptConfig.load()

    db.create_all_table()

    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "IT Asset Management REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/asset-management/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "krishna261152921044102586974899032980882739636"
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )
    
    # @jwt.token_in_blocklist_loader
    # def check_if_token_in_blocklist(jwt_header, jwt_payload):
    #     return jwt_payload["jti"] in BLOCKLIST


    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    api.register_blueprint(AuthRoutes,url_prefix="/asset-management")
    api.register_blueprint(UserRoutes,url_prefix="/asset-management")
    api.register_blueprint(CategoryRoutes,url_prefix="/asset-management")
    api.register_blueprint(VendorRoutes,url_prefix="/asset-management")
    api.register_blueprint(AssetRoutes,url_prefix="/asset-management")
    api.register_blueprint(IssueRoutes,url_prefix="/asset-management")

    return app