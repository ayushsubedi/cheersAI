from cheersAI import application
from flask import render_template, request, flash
from cheersAI import basic_auth
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_uploads.exceptions import UploadNotAllowed
from cheersAI.helper import transform_image



@application.route("/all_patients", methods=['GET'])
@basic_auth.required
def all_patients():
    return render_template('all_patients.html')


@application.route('/')
def index():
    return render_template("dashboard.html")
