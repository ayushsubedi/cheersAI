from cheersAI import application
from flask import render_template, request, jsonify, flash, redirect, url_for
from cheersAI.forms import PatientForm
from cheersAI.models import Patient
from cheersAI import db
import pandas as pd
from datetime import datetime

@application.route("/all_patients", methods=['GET'])
def all_patients():
    patients = Patient.query.all()
    return render_template('all_patients.html', patients=patients)


@application.route("/patient/create", methods=['GET', 'POST'])
def patient_create():
    form = PatientForm()
    if form.validate_on_submit():
        new_patient = Patient(
            first_name=request.form['first_name'], 
            last_name=request.form['last_name'], 
            age=request.form['age'], 
            gender=request.form['gender'], 
            address=request.form['address'],
            country=request.form['country'],
            cheers_id=request.form['cheers_id'])
        try:
            db.session.add(new_patient)
            db.session.commit()
            flash (f"Patient created successfully.", "success")
        except Exception as e:
            flash (f"Something went wrong."+str(e), "danger")
        finally:
            return redirect(url_for('all_patients'))
    return render_template('create_patient.html', action='patient_create', form=form)


@application.route("/patient/delete/<patient_id>", methods=['GET'])
def patient_delete(patient_id):
    del_patient = Patient.query.filter_by(id=patient_id).first_or_404()
    try:
        db.session.delete(del_patient)
        db.session.commit()
        flash (f"Patient deleted successfully.", "success")
    except Exception as e:
        flash (f"Something went wrong."+str(e), "danger")
    finally:
        return redirect(url_for('all_patients'))


@application.route("/patient/edit/<patient_id>", methods=['GET', 'POST'])
def patient_edit(patient_id):
    edit_patient = Patient.query.filter_by(id=patient_id).first_or_404()
    form = PatientForm(obj=edit_patient)
    if form.validate_on_submit():
        form.populate_obj(edit_patient)
        edit_patient['date_update'] = datetime.utcnow()
        try:
            db.session.commit()
            flash (f"Patient updated successfully.", "success")
        except Exception as e:
            flash (f"Something went wrong."+str(e), "danger")
        finally:
            return redirect(url_for('all_patients'))
    return render_template('create_patient.html', action='patient_edit', form=form, patient_id=patient_id)

