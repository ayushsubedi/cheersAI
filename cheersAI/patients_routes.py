from cheersAI import application
from flask import render_template, request


@application.route("/all_patients", methods=['GET'])
def all_patients():
    return render_template('all_patients.html')
