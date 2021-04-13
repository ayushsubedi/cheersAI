from cheersAI import application
from flask import render_template, request, flash



@application.route("/all_patients", methods=['GET'])
def all_patients():
    return render_template('all_patients.html')


@application.route('/')
def index():
    return render_template("dashboard.html")
