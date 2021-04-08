from cheersAI import application
from flask import render_template
from cheersAI import basic_auth

@application.route('/')
def index():
    return render_template("dashboard.html")

@application.route('/dr')
@basic_auth.required
def dr():
    return render_template("dr.html")

@application.route('/glaucoma')
@basic_auth.required
def glaucoma():
    return render_template("glaucoma.html")
