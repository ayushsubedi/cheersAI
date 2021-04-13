
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

