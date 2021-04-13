from cheersAI import application
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

country_list = ['Nepal', 'India', 'Other South Asian Country', 'Other']

class PatientForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    cheers_id = StringField('Cheers ID', validators=[Length(min=2, max=50)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=50)])
    gender = SelectField('Gender', choices=['Not Specified', 'Male', 'Female'], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), Length(min=2, max=50)])
    country = SelectField('Country', choices=country_list, validators=[DataRequired()])
    submit  = SubmitField('Add Patient')

