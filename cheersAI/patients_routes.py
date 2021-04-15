from cheersAI import application
from flask import render_template, request, jsonify, flash, redirect, url_for
from cheersAI.forms import PatientForm, DRForm
from cheersAI.models import Patient, DR
from cheersAI.helper import new_filename
from cheersAI import db
import pandas as pd
from datetime import datetime
from werkzeug.utils import secure_filename

DR_PATH = "cheersAI/static/uploaded_img/dr/"

@application.route("/all_patients", methods=['GET'])
def all_patients():
    patients = Patient.query.all()
    return render_template('all_patients.html', patients=patients)

@application.route("/patient/<patient_id>", methods=['GET', 'POST'])
def patient(patient_id):
    drform = DRForm()
    patient = Patient.query.filter_by(id=patient_id).first_or_404()
    drhistory = DR.query.filter_by(patient_id=patient_id)
    if drform.validate_on_submit():
        if (drform.left_eye.data or drform.left_eye.data):
            prediction_left, prediction_right = -1, -1
            left_eye_filename, right_eye_filename = "", ""
            if (drform.left_eye.data):
                left_eye_filename = secure_filename(drform.left_eye.data.filename)
                left_eye_filename = new_filename(patient_id, "left", left_eye_filename)
                drform.left_eye.data.save(DR_PATH + left_eye_filename)
                prediction_left = 0

            if (drform.right_eye.data):
                right_eye_filename = secure_filename(drform.right_eye.data.filename)
                right_eye_filename = new_filename(patient_id, "right", right_eye_filename)
                drform.right_eye.data.save(DR_PATH + right_eye_filename)
                prediction_right = 0

            new_dr = DR(
                patient_id = patient_id,
                prediction_left = prediction_left,
                image_left = left_eye_filename,
                prediction_right = prediction_right,
                image_right = right_eye_filename)
            try:
                db.session.add(new_dr)
                db.session.commit()
                flash (f"Added to patient history successfully.", "success")
            except Exception as e:
                flash (f"Something went wrong."+str(e), "danger")
            finally:
                return redirect(url_for('patient', patient_id=patient_id))
        else:
            flash (f"Upload left or right eye image to proceed.", "danger")
            return redirect(url_for('patient', patient_id=patient_id))
    return render_template('patient.html', patient=patient, drhistory=drhistory, drform=drform)


@application.route("/patient/create", methods=['GET', 'POST'])
def patient_create():
    form = PatientForm()
    if form.validate_on_submit():
        new_patient = Patient(
            first_name=request.form['first_name'], 
            last_name=request.form['last_name'], 
            age=request.form['age'], 
            email=request.form['email'],
            phone=request.form['phone'],
            gender=request.form['gender'], 
            address=request.form['address'],
            country=request.form['country'],
            cheers_id=request.form['cheers_id'])
        try:
            db.session.add(new_patient)
            db.session.commit()
            flash (f"Patient created successfully.", "success")
            return redirect(url_for('patient', patient_id=new_patient.id))
        except Exception as e:
            flash (f"Something went wrong."+str(e), "danger")
            return redirect(url_for('all_patients'))    
    return render_template('create_patient.html', title="Create New Patient", action='patient_create', form=form)


@application.route("/patient/delete/<patient_id>", methods=['GET'])
def patient_delete(patient_id):
    del_patient = Patient.query.filter_by(id=patient_id).first_or_404()
    delete_images = DR.__table__.delete().where(DR.patient_id == patient_id)
    try:
        db.session.delete(del_patient)
        db.session.execute(delete_images)
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
    return render_template('create_patient.html', action='patient_edit', title="Update Patient", form=form, patient_id=patient_id)

