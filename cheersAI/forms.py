from cheersAI import application
from cheersAI.helper import all_countries
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class PatientForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    cheers_id = StringField('Cheers ID')
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=50)])
    gender = SelectField('Gender', choices=['Not Specified', 'Male', 'Female'], validators=[DataRequired()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=150)])
    country = SelectField('Country', choices=all_countries())
    submit  = SubmitField('Add Patient')

