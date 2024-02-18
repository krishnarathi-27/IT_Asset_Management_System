import logging
from flask import Flask
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import Database
from config.flask_config import create_flask_config, register_blueprints, intialise_jwt_config

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.DEBUG,
    filename=AppConfig.LOG_LOCATION,
)

logger = logging.getLogger("main")

# def internal_server_error(e):
#   return {"message": 'huhuhu'}, 400

def create_app():
    """Creating flask app server and initialising all configs and database tables """
    logger.info('Creating flask app')
    
    print(AppConfig.PROMPT_FILE_LOCATION)
    PromptConfig.load()
    db = Database()
    db.create_all_table()

    app = Flask(__name__)
    # app.register_error_handler(404, internal_server_error)
    
    create_flask_config(app)
    intialise_jwt_config(app)
    register_blueprints(app)

    return app
