import pytest
from unittest.mock import MagicMock, patch
from app.predictor import predict_heart_disease

@patch("app.predictor.PreProcessor")
@patch("app.predictor.Pipeline")
def test_predict_heart_disease_true(mock_pipeline_cls, mock_preprocessor_cls):
  mock_preprocessor = MagicMock()
  mock_preprocessor.prepare_form.return_value = "processed_data"
  mock_preprocessor_cls.return_value = mock_preprocessor

  mock_model = MagicMock()
  mock_model.predict.return_value = [1]
  mock_pipeline = MagicMock()
  mock_pipeline.model = mock_model
  mock_pipeline_cls.return_value = mock_pipeline

  input_data = {"some": "data"}

  result = predict_heart_disease(input_data)

  mock_preprocessor.prepare_form.assert_called_once_with(input_data)
  mock_model.predict.assert_called_once_with("processed_data")
  assert result is True

@patch("app.predictor.PreProcessor")
@patch("app.predictor.Pipeline")
def test_predict_heart_disease_false(mock_pipeline_cls, mock_preprocessor_cls):
  mock_preprocessor = MagicMock()
  mock_preprocessor.prepare_form.return_value = "processed_data"
  mock_preprocessor_cls.return_value = mock_preprocessor

  mock_model = MagicMock()
  mock_model.predict.return_value = [0]
  mock_pipeline = MagicMock()
  mock_pipeline.model = mock_model
  mock_pipeline_cls.return_value = mock_pipeline

  input_data = {"some": "data"}

  result = predict_heart_disease(input_data)

  mock_preprocessor.prepare_form.assert_called_once_with(input_data)
  mock_model.predict.assert_called_once_with("processed_data")
  assert result is False
