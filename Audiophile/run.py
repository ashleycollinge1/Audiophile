#!/usr/bin/env python
from app import create_app, cli
from settings import Config

app = create_app()
cli.register(app)

if Config.FLASK_ENV == 'development':
    app.run(host=Config.HOST, port=Config.PORT, debug=True)

if Config.FLASK_ENV == 'production':
    app.run(host=Config.HOST, port=Config.PORT)