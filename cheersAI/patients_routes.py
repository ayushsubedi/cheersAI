from cheersAI import application
from flask import render_template, request


@application.route("/all_patients", methods=['GET'])
def all_patients():
    return render_template('all_patients.html')

@application.route("/create_patient", methods=['GET'])
def create_patient():
    return render_template('create_patient.html')
