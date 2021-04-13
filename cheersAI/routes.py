from cheersAI import application
from flask import render_template, request

@application.route('/')
def index():
    return render_template("dashboard.html")
