from flask import Flask
from os import environ
from flask_basicauth import BasicAuth

application = Flask(__name__)
basic_auth = BasicAuth(application)

# Secret key for form
application.config['SECRET_KEY'] = environ.get('SECRET_KEY')

# Basic auth
application.config['BASIC_AUTH_USERNAME'] = environ.get('BASIC_AUTH_USERNAME')
application.config['BASIC_AUTH_PASSWORD'] = environ.get('BASIC_AUTH_PASSWORD')

from cheersAI import routes