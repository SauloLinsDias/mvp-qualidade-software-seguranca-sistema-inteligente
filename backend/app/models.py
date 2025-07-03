from app.extensions import db

import datetime

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    chest_pain_type = db.Column(db.String(10), nullable=False)
    resting_bp = db.Column(db.Integer, nullable=False)
    cholesterol = db.Column(db.Integer, nullable=False)
    fasting_bs = db.Column(db.Integer, nullable=False)
    resting_ecg = db.Column(db.String(50), nullable=False)
    max_hr = db.Column(db.Integer, nullable=False)
    exercise_angina = db.Column(db.Boolean, nullable=False)
    oldpeak = db.Column(db.Float, nullable=False)
    st_slope = db.Column(db.String(10), nullable=False)
    heart_disease = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name:str, age:int, sex:str, chest_pain_type:str, resting_bp:int,
                 cholesterol:int, fasting_bs:int, resting_ecg:str, max_hr:int,
                 exercise_angina:bool, oldpeak:float, st_slope:str, heart_disease:int):
        self.name = name
        self.age = age
        self.sex = sex
        self.chest_pain_type = chest_pain_type
        self.resting_bp = resting_bp
        self.cholesterol = cholesterol
        self.fasting_bs = fasting_bs
        self.resting_ecg = resting_ecg
        self.max_hr = max_hr
        self.exercise_angina = exercise_angina
        self.oldpeak = oldpeak
        self.st_slope = st_slope
        self.heart_disease = heart_disease
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        return f"<Patient {self.name}, Age: {self.age}, Heart Disease: {self.has_heart_disease}>"

    def to_dict(self):
        return {
          "id": self.id,
          "name": self.name,
          "age": self.age,
          "sex": self.sex,
          "chest_pain_type": self.chest_pain_type,
          "resting_bp": self.resting_bp,
          "cholesterol": self.cholesterol,
          "fasting_bs": self.fasting_bs,
          "resting_ecg": self.resting_ecg,
          "max_hr": self.max_hr,
          "exercise_angina": self.exercise_angina,
          "oldpeak": self.oldpeak,
          "st_slope": self.st_slope,
          "heart_disease": self.heart_disease,
          "created_at": self.created_at,
      }

