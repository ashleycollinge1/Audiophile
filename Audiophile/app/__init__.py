from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
#from flask_bootstrap import Bootstrap

from app.frontend.routes import frontend
from app.api.routes import api


#bootstrap = Bootstrap()


def create_app(config_name, db):

    # create app instance
    app = Flask(__name__)

    # add configuration
    app.config.from_object(config_name)

    # register extensions
    #bootstrap.init_app(app)
    db.app = app
    db.init_app(app)

    # Swagger configuration
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Audiophile"
        }
    )
    

    # register blueprints
    app.register_blueprint(frontend)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    return app


"""
first, import db to setup app context
from run import db
then, import model to use it with queries
from app.models import User
"""