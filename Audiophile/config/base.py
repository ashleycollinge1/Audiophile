from .env import ENV_BOOL, ENV_STR, ABS_PATH

DEBUG = ENV_BOOL('DEBUG', False)
SECRET_KEY = ENV_STR('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + ABS_PATH(ENV_STR('SQLALCHEMY_DATABASE_URI'))
SQLALCHEMY_TRACK_MODIFICATIONS = True