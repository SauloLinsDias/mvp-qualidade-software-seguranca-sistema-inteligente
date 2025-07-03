COLUMNS = [
    'age',
    'sex',
    'chest_pain_type',
    'resting_bp',
    'cholesterol',
    'fasting_bs',
    'resting_ecg',
    'max_hr',
    'exercise_angina',
    'oldpeak',
    'st_slope'
]

class PreProcessor:
    def __init__(self):
        """Inicializa o preprocessador"""
        pass

    def prepare_form(self, form ):
        """Prepara o formulário para predição, convertendo campos binários e categóricos"""
        # Excluir colunas que não são necessárias para a predição
        form = {k: v for k, v in form.items() if k in COLUMNS}

        # Garante que todos os campos necessários estejam presentes
        for col in COLUMNS:
            if col not in form:
                raise ValueError(f"Campo obrigatório ausente: {col}")

        # Conversão dos campos categóricos e binários
        form = form.copy()
        form["sex"] = {'M': 0, 'F': 1}.get(form["sex"], 0)
        form["chest_pain_type"] = {'ATA': 0, 'NAP': 1, 'ASY': 2, 'TA': 3}.get(form["chest_pain_type"], 0)
        form["resting_ecg"] = {'Normal': 0, 'ST': 1, 'LVH': 2}.get(form["resting_ecg"], 0)
        form["st_slope"] = {'Up': 0, 'Flat': 1, 'Down': 2}.get(form["st_slope"], 0)
        form["exercise_angina"] = int(form["exercise_angina"]) if isinstance(form["exercise_angina"], (int, float, str)) else 0
        form["fasting_bs"] = int(form["fasting_bs"] > 120)

        # Garante que todas as colunas esperadas estejam presentes
        values = [form.get(col, 0) for col in COLUMNS]
        return [values]
