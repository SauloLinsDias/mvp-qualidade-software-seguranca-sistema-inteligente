import joblib

class Pipeline:
  def __init__(self, model_path: str):
    self.model = self.load_model(model_path)

  def load_model(self, model_path: str):
    """Load the trained model from a file."""
    with open(model_path, 'rb') as file:
      model = joblib.load(file)
    return model

  def load_scaler(self, scaler_path: str):
    """Load the scaler from a file."""
    with open(scaler_path, 'rb') as file:
      scaler = joblib.load(file)
    return scaler
