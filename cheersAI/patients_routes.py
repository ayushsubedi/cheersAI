from cheersAI import application
from flask import render_template, request, jsonify
from cheersAI.forms import PatientForm


@application.route("/all_patients", methods=['GET'])
def all_patients():
    return render_template('all_patients.html')

@application.route("/patient/create", methods=['GET', 'POST'])
def patient_create():
    if request.method == 'POST':
        print (jsonify(request.form))
    return render_template('create_patient.html')

@application.route("/patient/create2", methods=['GET', 'POST'])
def patient_create2():
    form = PatientForm()
    return render_template('create_patient_wtf.html', form=form)
