from cheersAI import application
from flask import render_template, request
from cheersAI.forms import LoginForm

@application.route("/all_users", methods=['GET'])
def all_users():
    return render_template('all_users.html')

# @application.route("/patient/create", methods=['GET', 'POST'])
# def patient_create():
#     form = PatientForm()
#     if form.validate_on_submit():
#         new_patient = Patient(
#             first_name=request.form['first_name'], 
#             last_name=request.form['last_name'], 
#             age=request.form['age'], 
#             email=request.form['email'],
#             phone=request.form['phone'],
#             gender=request.form['gender'], 
#             address=request.form['address'],
#             country=request.form['country'],
#             cheers_id=request.form['cheers_id'])
#         try:
#             db.session.add(new_patient)
#             db.session.commit()
#             flash (f"Patient created successfully.", "success")
#             return redirect(url_for('patient', patient_id=new_patient.id))
#         except Exception as e:
#             flash (f"Something went wrong."+str(e), "danger")
#             return redirect(url_for('all_patients'))    
#     return render_template('create_patient.html', title="Create New Patient", action='patient_create', form=form)



@application.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        print (email, password)
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

