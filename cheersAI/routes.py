from cheersAI import application
from flask import render_template


@application.route('/')
def index():
    return render_template("dashboard.html")

@application.route('/dr')
def dr():
    return render_template("dr.html")

@application.route('/glaucoma')
def glaucoma():
    return render_template("glaucoma.html")
