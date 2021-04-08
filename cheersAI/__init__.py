from flask import Flask
from os import environ
from flask_basicauth import BasicAuth
from flasgger import Swagger

application = Flask(__name__)
basic_auth = BasicAuth(application)

# Secret key for form
application.config['SECRET_KEY'] = environ.get('SECRET_KEY')

# Basic auth
application.config['BASIC_AUTH_USERNAME'] = environ.get('BASIC_AUTH_USERNAME')
application.config['BASIC_AUTH_PASSWORD'] = environ.get('BASIC_AUTH_PASSWORD')

template = {
    "swagger": "2.0",
    "info": {
        "title": "cheersAI API Documentation",
        "description": "APIs for cheersAI diabetic retinopathy and glaucoma prediction.",
    }
}

application.config['SWAGGER'] = {
    'title': 'CheersAI API',
    'uiversion': 3
}

swagger = Swagger(application, template=template)
from cheersAI import routes
from cheersAI import api