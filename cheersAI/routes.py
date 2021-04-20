from cheersAI import application
from flask import render_template, request
from cheersAI.helper import login_required

@application.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@application.route('/')
def index():
    return render_template("index.html")
