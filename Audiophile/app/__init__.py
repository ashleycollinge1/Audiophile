from app.api.models import db
from flask import Flask
#from flask_bootstrap import Bootstrap
from config import base
from app.frontend.routes import frontend
from app.api.routes import api
from app.api.models import User
from sqlalchemy_utils import database_exists, create_database


from flask_migrate import Migrate


def create_app():

    # create app instance
    app = Flask(__name__)

    # add configuration
    config_name = base
    app.config.from_object(config_name)

    # register extensions
    #bootstrap.init_app(app)
    db.app = app
    db.init_app(app)

    # setup flask-migrate
    migrate = Migrate(app, db)

    with app.app_context():
        print(base.SQLALCHEMY_DATABASE_URI)
        if not database_exists(base.SQLALCHEMY_DATABASE_URI):
            create_database(base.SQLALCHEMY_DATABASE_URI)
        db.create_all()
        # creates user if one doesn't exist
        print("hello")
        if User.query.all() is None:
            usr = User(name='user2', description='')
            db.session.add(usr)
            db.session.commit()
        print(User.query.filter_by(name='user'))
        if User.query.filter_by(name='user') is None:
            print("hello2")


    # register blueprints
    app.register_blueprint(frontend)
    app.register_blueprint(api, url_prefix='/api')
    return app
