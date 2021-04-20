from cheersAI import application
from flask import render_template, request, jsonify, flash, redirect, url_for, session
from cheersAI.forms import LoginForm, RegisterForm
from cheersAI.models import User
from cheersAI import db
from cheersAI import basic_auth


@application.route("/all_users", methods=['GET'])
@basic_auth.required
def all_users():
    users = User.query.all()
    return render_template('all_users.html', users=users)


@application.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first_or_404()
        if (user.password==password):
            flash (f"Login Successful.", "success")
            return redirect(url_for('index'))
        else:
            flash (f"Incorrect username or password.", "danger")
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@application.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logout Successful!")
    return redirect(url_for('login'))


@application.route("/register", methods=['GET', 'POST'])
@basic_auth.required
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            email = request.form['email'],
            password = request.form['password'],
            is_admin = request.form.get('is_admin', '')=='y')
        try:
            db.session.add(new_user)
            db.session.commit()
            flash (f"User created successfully.", "success")
            return redirect(url_for('index'))
        except Exception as e:
            flash (f"Something went wrong."+str(e), "danger")
            return redirect(url_for('index'))    
    return render_template('register.html', form=form)



@application.route("/user/delete/<user_id>", methods=['GET'])
@basic_auth.required
def user_delete(user_id):
    del_user = User.query.filter_by(id=user_id).first_or_404()
    try:
        db.session.delete(del_user)
        db.session.commit()
        flash (f"User deleted successfully.", "success")
    except Exception as e:
        flash (f"Something went wrong."+str(e), "danger")
    finally:
        return redirect(url_for('all_users'))


