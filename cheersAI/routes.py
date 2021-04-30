from cheersAI import application
from flask import render_template, request
from cheersAI.helper import login_required


@application.route('/')
def index():
    return render_template("index.html")
