from app.api.models import db
from flask import Flask
from settings import Config
from app.frontend.routes import frontend
from app.api.routes import api
from app.api.models import User
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate
from app import cli

def create_app():

    # create app instance
    app = Flask(__name__)

    # add configuration
    app.config.from_object(Config)

    # register extensions
    #bootstrap.init_app(app)
    db.app = app
    db.init_app(app)

    # setup flask-migrate
    migrate = Migrate(app, db)

    with app.app_context():
        if not database_exists(Config.SQLALCHEMY_DATABASE_URI):
            create_database(Config.SQLALCHEMY_DATABASE_URI)
        db.create_all()
        # creates user if one doesn't exist
        if User.query.all() is None:
            usr = User(name='user2', description='')
            db.session.add(usr)
            db.session.commit()
        if User.query.filter_by(name='user') is None:
            pass


    # register blueprints
    app.register_blueprint(frontend)
    app.register_blueprint(api, url_prefix='/api')

    cli.register(app)
    return app
