from cheersAI import application
from cheersAI import db
from datetime import datetime

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cheers_id = db.Column(db.String(50), nullable=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=True)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)
    date_update = db.Column(db.DateTime, default=datetime.utcnow)
   

    def __repr__(self):
        return f"<id={self.id}>"

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)


class DR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    prediction_left = db.Column(db.String(100))
    prediction_left_all = db.Column(db.String(100))
    image_left = db.Column(db.String(20), nullable=True)
    prediction_right = db.Column(db.String(100))
    prediction_right_all = db.Column(db.String(100))
    image_right = db.Column(db.String(20), nullable=True)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)
        
    def __repr__(self):
        return f"<id={self.id}>"

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    is_admin =  db.Column(db.Boolean, default=False)
    date_create = db.Column(db.DateTime, default=datetime.utcnow)
        
    def __repr__(self):
        return f"<id={self.id}>"

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)
    