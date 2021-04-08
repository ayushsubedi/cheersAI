from cheersAI import application
from flask import render_template, request, flash
from cheersAI import basic_auth
from flask_uploads import IMAGES, UploadSet, configure_uploads

photos = UploadSet("photos", IMAGES)

configure_uploads(application, photos)

@application.route("/dr", methods=['GET', 'POST'])
@basic_auth.required
def dr():
    if request.method == 'POST' and 'photo' in request.files:
        photos.save(request.files['photo'])
        flash("Photo saved successfully.")
        return render_template('dr.html')
    return render_template('dr.html')


@application.route('/')
def index():
    return render_template("dashboard.html")


@application.route('/glaucoma')
@basic_auth.required
def glaucoma():
    return render_template("glaucoma.html")
