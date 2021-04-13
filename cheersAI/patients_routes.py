from cheersAI import application
from flask import render_template, request, jsonify
from cheersAI.forms import PatientForm


@application.route("/all_patients", methods=['GET'])
def all_patients():
    return render_template('all_patients.html')


@application.route("/patient/create", methods=['GET', 'POST'])
def patient_create():
    form = PatientForm()
    return render_template('create_patient.html', form=form)

