from cheersAI import application
from flask import render_template, request, flash
from cheersAI import basic_auth
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_uploads.exceptions import UploadNotAllowed
from cheersAI.helper import transform_image

photos = UploadSet("photos")

configure_uploads(application, photos)

@application.route("/dr", methods=['GET', 'POST'])
@basic_auth.required
def dr():
    filename_left, filename_right = None, None
    if request.method == 'POST' and ('photo_left' or 'photo_right') in request.files:
        try:
            filename_left = photos.save(request.files['photo_left'])
            filename_right = photos.save(request.files['photo_right'])
            flash("Photo saved successfully.")
        except UploadNotAllowed:
            flash("Failed. Please select jpeg, jpg or png.")
        content = {
            "filename_left":filename_left, 
            "filename_right":filename_right, 
            "prediction_left":transform_image('cheersAI/static/uploaded_img/'+filename_left),
            "prediction_right":transform_image('cheersAI/static/uploaded_img/'+filename_left)
        }
        return render_template('dr.html', **content)
    return render_template('dr.html')


@application.route('/')
def index():
    return render_template("dashboard.html")


@application.route('/glaucoma')
@basic_auth.required
def glaucoma():
    return render_template("glaucoma.html")
