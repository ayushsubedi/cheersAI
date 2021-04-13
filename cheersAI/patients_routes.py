from cheersAI import application
from flask import render_template, request, jsonify, flash, redirect, url_for
from cheersAI.forms import PatientForm
from cheersAI.models import Patient
from cheersAI import db


@application.route("/all_patients", methods=['GET'])
def all_patients():
    return render_template('all_patients.html')


@application.route("/patient/create", methods=['GET', 'POST'])
def patient_create():
    form = PatientForm()
    if form.validate_on_submit():
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        gender = request.form['gender']
        address = request.form['address']
        country = request.form['country']
        cheers_id = request.form['cheers_id']
        print (request.form.items)
        new_patient = Patient(
            first_name=first_name, 
            last_name=last_name, 
            age=age, 
            gender=gender, 
            address=address,
            country=country,
            cheers_id=cheers_id)
        try:
            db.session.add(new_patient)
            db.session.commit()
            flash (f"Patient created successfully.", "success")
            return redirect(url_for('all_patients'))
        except Exception as e:
            flash (f"Something went wrong."+str(e), "danger")
            return redirect(url_for('all_patients'))
    return render_template('create_patient.html', form=form)

