from cheersAI import application
from flask import render_template, request


@application.route("/all_users", methods=['GET'])
def all_users():
    return render_template('all_users.html')


