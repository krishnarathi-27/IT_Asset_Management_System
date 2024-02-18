import logging
from flask import jsonify
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from routes.auth_routes import blp as AuthRoutes
from routes.user_routes import blp as UserRoutes
from routes.category_routes import blp as CategoryRoutes
from routes.vendor_routes import blp as VendorRoutes
from routes.asset_routes import blp as AssetRoutes
from routes.issue_routes import blp as IssueRoutes
from utils.token import Token

logger = logging.getLogger('flask_config')

def create_flask_config(app):
    """ Creates all flask config for flask app and Swagger documentation """
    logger.info('Setting all flask and swagger configs')

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "IT Asset Management REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/asset-management/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    app.config["JWT_SECRET_KEY"] = "krishna261152921044102586974899032980882739636"

def intialise_jwt_config(app):
    """Initialising all jwt inbuilt decorators"""
    logger.info('Intialising all jwt decorators')

    jwt = JWTManager(app)
    token_obj = Token()

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
    
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        check_access_revoked = token_obj.check_token_revoked(jwt_payload,'access_token')
        check_refresh_revoked = token_obj.check_token_revoked(jwt_payload,'refresh_token')
        return check_access_revoked or check_refresh_revoked
    
def register_blueprints(app):
    'Register blueprints to flask app'
    logger.info('Registring all flask blueprints')

    api = Api(app)

    api.register_blueprint(AuthRoutes)
    api.register_blueprint(UserRoutes)
    api.register_blueprint(CategoryRoutes)
    api.register_blueprint(VendorRoutes)
    api.register_blueprint(AssetRoutes)
    api.register_blueprint(IssueRoutes)
    