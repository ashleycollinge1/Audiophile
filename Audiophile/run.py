#!/usr/bin/env python

# model import is required to set up database correctly

from app import create_app
from config import base


app = create_app()

from app.api.models import db
from app.api.models import User

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
