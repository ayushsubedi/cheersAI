from cheersAI import application
from flask import render_template, request


@application.route("/all_patients", methods=['GET'])
def all_patients():
    return render_template('all_patients.html')

@application.route("/patient/create", methods=['GET'])
def patient_create():
    return render_template('create_patient.html')
