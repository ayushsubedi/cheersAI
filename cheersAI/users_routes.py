from cheersAI import application
from flask import render_template, request, jsonify, flash, redirect, url_for
from cheersAI.forms import LoginForm


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

