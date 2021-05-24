from flask import Flask
import os
from os.path import join, dirname
from os import environ
from flask_basicauth import BasicAuth
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# import pymysql
# pymysql.install_as_MySQLdb()
sentry_sdk.init(
    dsn="https://13ddaefce4a44877ae4ff3ab2ccf76a9@o717172.ingest.sentry.io/5779777",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

application = Flask(__name__)
basic_auth = BasicAuth(application)

dotenv_path = join(dirname(__file__),'..','.env')
load_dotenv(dotenv_path)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cheersai.db'
# application.config['SQLALCHEMY_DATABASE_URI'] = "mysql://O7bXLfCUEy:YMXDVMsGgg@remotemysql.com:3306/O7bXLfCUEy"

db = SQLAlchemy(application)
# Secret key for form
application.config['SECRET_KEY'] = environ.get('SECRET_KEY')

# Basic auth
application.config['BASIC_AUTH_USERNAME'] = environ.get('BASIC_AUTH_USERNAME')
application.config['BASIC_AUTH_PASSWORD'] = environ.get('BASIC_AUTH_PASSWORD')

application.config["UPLOADED_IMAGES_DEST"] = "cheersAI/static/uploaded_img"
application.config['UPLOADED_IMAGES_ALLOW'] = set(['png', 'jpg', 'jpeg'])
application.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


from cheersAI import routes
from cheersAI import models
from cheersAI import patients_routes
from cheersAI import users_routes
