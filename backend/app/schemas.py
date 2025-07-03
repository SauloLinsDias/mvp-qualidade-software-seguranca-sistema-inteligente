from pydantic import BaseModel
from typing import Literal, List

class PatientInput(BaseModel):
    name: str
    age: int
    sex: Literal["M", "F"]
    chest_pain_type: Literal["ATA", "ASY", "NAP", "TA"]
    resting_bp: float
    cholesterol: float
    fasting_bs: float
    resting_ecg: Literal["Normal", "ST", "LVH"]
    max_hr: float
    exercise_angina: bool
    oldpeak: float
    st_slope: Literal["Up", "Flat", "Down"]

class PatientOutput(BaseModel):
    id: int
    name: str
    age: int
    sex: Literal["M", "F"]
    chest_pain_type: Literal["ATA", "ASY", "NAP", "TA"]
    resting_bp: float
    cholesterol: float
    fasting_bs: float
    resting_ecg: Literal["Normal", "ST", "LVH"]
    max_hr: float
    exercise_angina: bool
    oldpeak: float
    st_slope: Literal["Up", "Flat", "Down"]
    heart_disease: bool
    created_at: str

class PatientListOutput(BaseModel):
    patients: List[PatientOutput]

class PredictionOutput(BaseModel):
    heart_disease: bool

class PatientPathParams(BaseModel):
    patient_id: int
