from cheersAI import application
from cheersAI.helper import all_countries
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, NumberRange, Email, Optional, EqualTo

from flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, IMAGES, configure_uploads

images = UploadSet('images', IMAGES)
configure_uploads(application, images)


class PatientForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    cheers_id = StringField('Cheers ID')
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=50)])
    gender = SelectField('Gender', choices=['Not Specified', 'Male', 'Female'], validators=[DataRequired()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=150)])
    email = EmailField('Email', validators=[Optional(), Email()])
    phone = StringField('Phone Number')
    country = SelectField('Country', choices=all_countries())
    submit = SubmitField('Save')


class DRForm(FlaskForm):
    left_eye = FileField('Left Eye', validators=[FileAllowed(images, 'Incorrect file type. Upload accepts images only.')])
    right_eye = FileField('Right Eye', validators=[FileAllowed(images, 'Incorrect file type. Upload accepts images only.')])
    submit_dr = SubmitField('Predict DR')


class GlaucomaForm(FlaskForm):
    left_eye = FileField('Left Eye', validators=[FileAllowed(images, 'Incorrect file type. Upload accepts images only.')])
    right_eye = FileField('Right Eye', validators=[FileAllowed(images, 'Incorrect file type. Upload accepts images only.')])
    submit_glaucoma = SubmitField('Predict Glaucoma')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[Email()])
    password = PasswordField('Password', [
        DataRequired(), EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    is_admin = BooleanField()
    submit = SubmitField('Register')
