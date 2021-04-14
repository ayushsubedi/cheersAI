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
    date_create = db.Column(db.DateTime, default=datetime.utcnow)
    date_update = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<id={self.id}, cheers_id={self.cheers_id}, first_name={self.first_name}, last_name={self.last_name}, age={self.age}, gender={self.gender}, address={self.address}, country={self.country}, date_create={self.date_create},  date_update={self.date_update}>"

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)