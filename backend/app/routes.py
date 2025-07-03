from flask_openapi3 import APIBlueprint, Tag
from app.schemas import PatientInput, PredictionOutput, PatientOutput, PatientListOutput, PatientPathParams
from app.extensions import db
from app.models import Patient
from app.predictor import predict_heart_disease

patients_tag = Tag(name='Patients', description='Operations related to patients and heart disease predictions')
patients_bp = APIBlueprint('patients', __name__, abp_tags=[patients_tag], url_prefix='/patients')

@patients_bp.get("/", responses={200: PatientListOutput})
def get_patients():
    patients = Patient.query.all()
    return [patient.to_dict() for patient in patients]

@patients_bp.get("/<int:patient_id>", responses={200: PatientOutput})
def get_patient(path: PatientPathParams):
    patient = Patient.query.get_or_404(path.patient_id)
    return patient.to_dict()

@patients_bp.post("/", responses={201: PredictionOutput})
def create_patient(body: PatientInput):
    data = body.dict()
    prediction = predict_heart_disease(data)

    patient = Patient(**data, heart_disease=prediction)
    db.session.add(patient)
    db.session.commit()

    return {"has_heart_disease": prediction}, 201

@patients_bp.put("/<int:patient_id>", responses={200: PatientOutput})
def update_patient(path: PatientPathParams, body: PatientInput):
    patient = Patient.query.get_or_404(path.patient_id)
    data = body.dict()

    for key, value in data.items():
        setattr(patient, key, value)

    prediction = predict_heart_disease(data)
    patient.has_heart_disease = prediction

    db.session.commit()

    return patient.to_dict()

@patients_bp.delete("/<int:patient_id>", responses={204: {}})
def delete_patient(path: PatientPathParams):
    patient = Patient.query.get_or_404(path.patient_id)
    db.session.delete(patient)
    db.session.commit()
    return {}, 204
