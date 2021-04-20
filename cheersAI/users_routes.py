from cheersAI import application
from flask import render_template, request


@application.route("/all_users", methods=['GET'])
def all_users():
    return render_template('all_users.html')

@application.route("/login", methods=['GET'])
def login():
    return render_template('login.html')


