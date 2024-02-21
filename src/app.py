from flask import Flask, g

def create_app():
    """Creating flask app server and initialising all configs and database tables """

    app = Flask(__name__)
    
    with app.app_context():
        from src.config.flask_config import (
            create_flask_config, 
            register_blueprints, 
            intialise_jwt_config,
            register_error
        )
        from src.config.prompts.prompts import PromptConfig
        from src.utils.common_helper import generate_shortuuid
        register_error(app)
        create_flask_config(app)
        intialise_jwt_config(app)
        register_blueprints(app)
        PromptConfig.load()

    @app.before_request
    def get_request_id() -> None:
        """
            Function that will be invoked before every request to reset request id.
            Parameters -> None
            Returns -> None
        """
        new_request_id = generate_shortuuid("REQ")
        g.request_id = new_request_id

    @app.route("/status", methods=["GET"])
    def status():
        return {
            "status": "API is working fine"
        }, 200

    return app

    return app
