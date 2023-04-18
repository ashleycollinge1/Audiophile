#!/usr/bin/env python

# model import is required to set up database correctly
from app.api.models import db, User
from app import create_app
from config import base
from sqlalchemy_utils import database_exists, create_database


app = create_app(base, db)


if __name__ == '__main__':
    with app.app_context():
        print(base.SQLALCHEMY_DATABASE_URI)
        if not database_exists(base.SQLALCHEMY_DATABASE_URI):
            create_database(base.SQLALCHEMY_DATABASE_URI)
            db.create_all()
        # creates user if one doesn't exist
        #if User.query.filter_by(name='user') is None:
        #    usr = User(name='user', description='')
        #    db.session.add(usr)
        #    db.session.commit()
    app.run(host='0.0.0.0', port=5000)
