
from cheersAI import application
from flask import Flask, request, jsonify
import datetime
from cheersAI.models import Patient
from cheersAI import db

@application.route('/api/test/', methods=['POST'])
def add_test():
      """Endpoint for test
    ---
    tags:
      - Test
    parameters:
      - name: body
        in: body
        required: true
        description:
        example: {
            "user_id": "fasdlfjasldf",
            "item_id": "asd2sdfsafdasd"
        }
    responses:
        200:
            description: everything works fine
        500:
            description: something went wrong
    """
      request_json = request.json
      return jsonify(request_json), 200


@application.route('/api/patient/create', methods=['POST'])
def api_patient_create():
      """Endpoint to create patient
    ---
    tags:
      - Patient
    parameters:
      - name: body
        in: body
        required: true
        description:
        example: {
            "first_name": "Ram",
            "last_name": "Gautam",
            "age": "23",
            "gender": "Male",
            "address": "Ratnanagar 13, Chitwan",
            "country": "Nepal"
        }
    responses:
        200:
            description: Patient created successfully
        500:
            description: Something went wrong
    """
      
      first_name = request.json['first_name']
      last_name = request.json['last_name']
      age = request.json['age']
      gender = request.json['gender']
      address = request.json['address']
      country = request.json['country']
      cheers_id = request.json['cheers_id']
      new_patient = Patient(
        first_name=first_name, 
        last_name=last_name, 
        age=age, 
        gender=gender, 
        address=address,
        country=country,
        cheers_id=cheers_id)
      try:
        db.session.add(new_patient)
        db.session.commit()
        return 'successful', 200
      except Exception as e:
        return str(e), 500
      return jsonify(request_json), 200