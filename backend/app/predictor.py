from app.preprocessor import PreProcessor
from app.pipeline import Pipeline

def predict_heart_disease(data: dict):
      preprocessor = PreProcessor()
      pipeline = Pipeline(model_path="heart_model.pkl")

      data = preprocessor.prepare_form(data)
      model = pipeline.model

      outcome = model.predict(data)

      return bool(outcome[0])
