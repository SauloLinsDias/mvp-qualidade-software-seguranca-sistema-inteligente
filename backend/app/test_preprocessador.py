import pytest
from app.preprocessor import PreProcessor, COLUMNS

@pytest.fixture
def valid_form():
  return {
    'age': 55,
    'sex': 'M',
    'chest_pain_type': 'NAP',
    'resting_bp': 140,
    'cholesterol': 200,
    'fasting_bs': 130,
    'resting_ecg': 'LVH',
    'max_hr': 150,
    'exercise_angina': '1',
    'oldpeak': 2.3,
    'st_slope': 'Flat'
  }

def test_prepare_form_valid(valid_form):
  pre = PreProcessor()
  result = pre.prepare_form(valid_form)
  assert isinstance(result, list)
  assert len(result) == 1
  values = result[0]
  assert len(values) == len(COLUMNS)
  # Check categorical conversions
  assert values[COLUMNS.index('sex')] == 0  # 'M' -> 0
  assert values[COLUMNS.index('chest_pain_type')] == 1  # 'NAP' -> 1
  assert values[COLUMNS.index('resting_ecg')] == 2  # 'LVH' -> 2
  assert values[COLUMNS.index('st_slope')] == 1  # 'Flat' -> 1
  assert values[COLUMNS.index('exercise_angina')] == 1  # '1' -> 1
  assert values[COLUMNS.index('fasting_bs')] == 1  # 130 > 120 -> 1

def test_prepare_form_missing_column(valid_form):
  pre = PreProcessor()
  form = valid_form.copy()
  form.pop('age')
  with pytest.raises(ValueError) as excinfo:
    pre.prepare_form(form)
  assert "Campo obrigatório ausente: age" in str(excinfo.value)

def test_prepare_form_extra_fields(valid_form):
  pre = PreProcessor()
  form = valid_form.copy()
  form['extra_field'] = 'should be ignored'
  result = pre.prepare_form(form)
  assert isinstance(result, list)
  assert len(result[0]) == len(COLUMNS)

@pytest.mark.parametrize("sex,expected", [('M', 0), ('F', 1), ('X', 0)])
def test_sex_conversion(valid_form, sex, expected):
  pre = PreProcessor()
  form = valid_form.copy()
  form['sex'] = sex
  result = pre.prepare_form(form)
  assert result[0][COLUMNS.index('sex')] == expected

@pytest.mark.parametrize("cp_type,expected", [('ATA', 0), ('NAP', 1), ('ASY', 2), ('TA', 3), ('UNK', 0)])
def test_chest_pain_type_conversion(valid_form, cp_type, expected):
  pre = PreProcessor()
  form = valid_form.copy()
  form['chest_pain_type'] = cp_type
  result = pre.prepare_form(form)
  assert result[0][COLUMNS.index('chest_pain_type')] == expected

@pytest.mark.parametrize("resting_ecg,expected", [('Normal', 0), ('ST', 1), ('LVH', 2), ('UNK', 0)])
def test_resting_ecg_conversion(valid_form, resting_ecg, expected):
  pre = PreProcessor()
  form = valid_form.copy()
  form['resting_ecg'] = resting_ecg
  result = pre.prepare_form(form)
  assert result[0][COLUMNS.index('resting_ecg')] == expected

@pytest.mark.parametrize("st_slope,expected", [('Up', 0), ('Flat', 1), ('Down', 2), ('UNK', 0)])
def test_st_slope_conversion(valid_form, st_slope, expected):
  pre = PreProcessor()
  form = valid_form.copy()
  form['st_slope'] = st_slope
  result = pre.prepare_form(form)
  assert result[0][COLUMNS.index('st_slope')] == expected

@pytest.mark.parametrize("exercise_angina,expected", [(1, 1), (0, 0), ('1', 1), ('0', 0), (None, 0)])
def test_exercise_angina_conversion(valid_form, exercise_angina, expected):
  pre = PreProcessor()
  form = valid_form.copy()
  form['exercise_angina'] = exercise_angina
  result = pre.prepare_form(form)
  assert result[0][COLUMNS.index('exercise_angina')] == expected

@pytest.mark.parametrize("fasting_bs,expected", [(121, 1), (120, 0), (100, 0), (200, 1)])
def test_fasting_bs_conversion(valid_form, fasting_bs, expected):
  pre = PreProcessor()
  form = valid_form.copy()
  form['fasting_bs'] = fasting_bs
  result = pre.prepare_form(form)
  assert result[0][COLUMNS.index('fasting_bs')] == expected
