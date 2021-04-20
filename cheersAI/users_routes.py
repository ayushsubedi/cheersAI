from cheersAI import application
from flask import render_template, request, jsonify, flash, redirect, url_for
from cheersAI.forms import LoginForm, RegisterForm
from cheersAI.models import User
from cheersAI import db

@application.route("/all_users", methods=['GET'])
def all_users():
    return render_template('all_users.html')


@application.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        flash (f"Login Successful.", "success")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

# @application.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         email = request.form['email']
#         password = request.form['password']
#         flash (f"Registration Successful.", "success")
#         return redirect(url_for('index'))
#     return render_template('login.html', form=form)

@application.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            email = request.form['email'],
            password = request.form['password'],
            is_admin = request.form['is_admin'])
        try:
            db.session.add(new_user)
            db.session.commit()
            flash (f"User created successfully.", "success")
            return redirect(url_for('index'))
        except Exception as e:
            flash (f"Something went wrong."+str(e), "danger")
            return redirect(url_for('index'))    
    return render_template('register.html', form=form)

