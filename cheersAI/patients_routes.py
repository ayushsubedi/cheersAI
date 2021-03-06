from cheersAI import application
from flask import render_template, request, flash, redirect, url_for, Response
from cheersAI.forms import PatientForm, DRForm, GlaucomaForm
from cheersAI.models import Patient, DR, Glaucoma
from cheersAI.helper import new_filename, transform_dr_image
from cheersAI.helper import transform_glaucoma_image, login_required
from cheersAI.helper import inference_dr, inference_glaucoma, image_is_blurry
from cheersAI.helper import image_is_dark
from cheersAI import db
from datetime import datetime
from werkzeug.utils import secure_filename
import pandas as pd

DR_PATH = "cheersAI/static/uploaded_img/dr/"
GLAUCOMA_PATH = "cheersAI/static/uploaded_img/glaucoma/"


@application.route("/download_patients", methods=['GET'])
@login_required
def download_patients():
    patients = Patient.query.all()
    patients_dict = [r.__dict__ for r in patients]
    df = pd.DataFrame.from_dict(patients_dict)
    return Response(
        df.iloc[:,1:].to_csv(index=False),
        mimetype="text/csv",
        headers={"Content-disposition":
        "attachment; filename=patients.csv"})

@application.route("/all_patients", methods=['GET'])
@login_required
def all_patients():
    patients = Patient.query.all()
    return render_template('all_patients.html', patients=patients)


@application.route("/patient/<patient_id>", methods=['GET', 'POST'])
@login_required
def patient(patient_id):
    drform = DRForm()
    glaucomaform = GlaucomaForm()    
    patient = Patient.query.filter_by(id=patient_id).first_or_404()
    drhistory = DR.query.filter_by(patient_id=patient_id).all()
    dict_dr_inference = inference_dr([r.__dict__ for r in drhistory])
    glaucomahistory = Glaucoma.query.filter_by(patient_id=patient_id).all()
    # TODO: inference
    dict_glaucoma_inference = inference_glaucoma(
        [r.__dict__ for r in glaucomahistory])

    if glaucomaform.validate_on_submit() and glaucomaform.submit_glaucoma.data:
        if (glaucomaform.left_eye.data or glaucomaform.right_eye.data):
            prediction_left, prediction_right = -1, -1
            prediction_left_all, prediction_right_all = "", ""
            left_eye_filename, right_eye_filename = "", ""
            if (glaucomaform.left_eye.data):
                left_eye_filename = secure_filename(
                    glaucomaform.left_eye.data.filename)
                left_eye_filename = new_filename(
                    patient_id, "left", left_eye_filename)
                glaucomaform.left_eye.data.save(
                    GLAUCOMA_PATH + left_eye_filename)
                if (image_is_dark(
                    GLAUCOMA_PATH + left_eye_filename) or image_is_blurry(
                        GLAUCOMA_PATH + left_eye_filename)):
                    flash("Image is not up to the par. It is either dark/bright or blurry.", "danger")
                    return redirect(url_for('patient', patient_id=patient_id))
                prediction_left_all, prediction_left = transform_glaucoma_image(
                    GLAUCOMA_PATH + left_eye_filename)

            if (glaucomaform.right_eye.data):
                right_eye_filename = secure_filename(glaucomaform.right_eye.data.filename)
                right_eye_filename = new_filename(patient_id, "right", right_eye_filename)
                glaucomaform.right_eye.data.save(GLAUCOMA_PATH + right_eye_filename)
                if (image_is_dark(GLAUCOMA_PATH + right_eye_filename) or image_is_blurry(GLAUCOMA_PATH + right_eye_filename)):
                    flash("Image is not up to the par. It is either dark/bright or blurry.", "danger")
                    return redirect(url_for('patient', patient_id=patient_id))
                prediction_right_all, prediction_right = transform_glaucoma_image(
                    GLAUCOMA_PATH + right_eye_filename)

            new_glaucoma = Glaucoma(
                patient_id=patient_id,
                prediction_left=prediction_left,
                prediction_left_all=prediction_left_all,
                image_left=left_eye_filename,
                prediction_right=prediction_right,
                prediction_right_all=prediction_right_all,
                image_right=right_eye_filename)
            try:
                db.session.add(new_glaucoma)
                db.session.commit()
                flash("Added to patient history successfully.", "success")
            except Exception as e:
                flash("Something went wrong."+str(e), "danger")
            finally:
                return redirect(url_for('patient', patient_id=patient_id))
        else:
            flash("Upload left or right eye image to proceed.", "danger")
            return redirect(url_for('patient', patient_id=patient_id))
    
    if drform.validate_on_submit() and drform.submit_dr.data:
        if (drform.left_eye.data or drform.right_eye.data):
            prediction_left, prediction_right = -1, -1
            prediction_left_all, prediction_right_all = "", ""
            left_eye_filename, right_eye_filename = "", ""
            if (drform.left_eye.data):
                left_eye_filename = secure_filename(drform.left_eye.data.filename)
                left_eye_filename = new_filename(patient_id, "left", left_eye_filename)
                drform.left_eye.data.save(DR_PATH + left_eye_filename)
                if (image_is_dark(DR_PATH + left_eye_filename) or image_is_blurry(DR_PATH + left_eye_filename)):
                    flash("Image is not up to the par. It is either dark/bright or blurry.", "danger")
                    return redirect(url_for('patient', patient_id=patient_id))
                prediction_left_all, prediction_left = transform_dr_image(DR_PATH + left_eye_filename)

            if (drform.right_eye.data):
                right_eye_filename = secure_filename(drform.right_eye.data.filename)
                right_eye_filename = new_filename(patient_id, "right", right_eye_filename)
                drform.right_eye.data.save(DR_PATH + right_eye_filename)
                if (image_is_dark(DR_PATH + right_eye_filename) or image_is_blurry(DR_PATH + right_eye_filename)):
                    flash("Image is not up to the par. It is either dark/bright or blurry.", "danger")
                    return redirect(url_for('patient', patient_id=patient_id))
                prediction_right_all, prediction_right = transform_dr_image(DR_PATH + right_eye_filename)

            new_dr = DR(
                patient_id=patient_id,
                prediction_left=prediction_left,
                prediction_left_all=prediction_left_all,
                image_left=left_eye_filename,
                prediction_right=prediction_right,
                prediction_right_all=prediction_right_all,
                image_right=right_eye_filename)
            try:
                db.session.add(new_dr)
                db.session.commit()
                flash("Added to patient history successfully.", "success")
            except Exception as e:
                flash("Something went wrong."+str(e), "danger")
            finally:
                return redirect(url_for('patient', patient_id=patient_id))
        else:
            flash("Upload left or right eye image to proceed.", "danger")
            return redirect(url_for('patient', patient_id=patient_id))
    return render_template('patient.html', patient=patient,drhistory=dict_dr_inference, drform=drform, glaucomahistory=dict_glaucoma_inference, glaucomaform=glaucomaform)


@application.route("/patient/create", methods=['GET', 'POST'])
@login_required
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
            flash("Patient created successfully.", "success")
            return redirect(url_for('patient', patient_id=new_patient.id))
        except Exception as e:
            flash("Something went wrong."+str(e), "danger")
            return redirect(url_for('all_patients'))
    return render_template('create_patient.html', title="Create New Patient", action='patient_create', form=form)


@application.route("/patient/delete/<patient_id>", methods=['GET'])
@login_required
def patient_delete(patient_id):
    del_patient = Patient.query.filter_by(id=patient_id).first_or_404()
    delete_images_dr = DR.__table__.delete().where(DR.patient_id == patient_id)
    delete_images_g = Glaucoma.__table__.delete().where(Glaucoma.patient_id == patient_id)
    try:
        db.session.delete(del_patient)
        db.session.execute(delete_images_dr)
        db.session.execute(delete_images_g)
        db.session.commit()
        flash("Patient deleted successfully.", "success")
    except Exception as e:
        flash("Something went wrong."+str(e), "danger")
    finally:
        return redirect(url_for('all_patients'))


@application.route("/dr/delete/<dr_id>", methods=['GET'])
@login_required
def dr_delete(dr_id):
    del_dr = DR.query.filter_by(id=dr_id).first_or_404()
    try:
        db.session.delete(del_dr)
        db.session.commit()
        flash("DR history deleted successfully.", "success")
    except Exception as e:
        flash("Something went wrong."+str(e), "danger")
    finally:
        return redirect(url_for('patient', patient_id=del_dr.patient_id))


@application.route("/glaucoma/delete/<glaucoma_id>", methods=['GET'])
@login_required
def glaucoma_delete(glaucoma_id):
    del_glaucoma = Glaucoma.query.filter_by(id=glaucoma_id).first_or_404()
    try:
        db.session.delete(del_glaucoma)
        db.session.commit()
        flash("Glaucoma history deleted successfully.", "success")
    except Exception as e:
        flash("Something went wrong."+str(e), "danger")
    finally:
        return redirect(url_for('patient', patient_id=del_glaucoma.patient_id))


@application.route("/patient/edit/<patient_id>", methods=['GET', 'POST'])
@login_required
def patient_edit(patient_id):
    edit_patient = Patient.query.filter_by(id=patient_id).first_or_404()
    form = PatientForm(obj=edit_patient)
    if form.validate_on_submit():
        form.populate_obj(edit_patient)
        edit_patient['date_update'] = datetime.utcnow()
        try:
            db.session.commit()
            flash("Patient updated successfully.", "success")
        except Exception as e:
            flash("Something went wrong."+str(e), "danger")
        finally:
            return redirect(url_for('all_patients'))
    return render_template('create_patient.html', action='patient_edit', title="Update Patient", form=form, patient_id=patient_id)
