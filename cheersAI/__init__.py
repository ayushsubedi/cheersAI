from flask import Flask
from os import environ


application = Flask(__name__)

from cheersAI import routes