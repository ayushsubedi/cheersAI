from cheersAI import application
from flask import render_template


@application.route('/')
def index():
    return 'future home of cheersAI'