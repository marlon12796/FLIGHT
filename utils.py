# utils.py
import pandas as pd
from global_env import REQUIRED_FIELDS


def validate_inputs(data):
    """Valida los inputs del usuario."""

    for field in REQUIRED_FIELDS:
        if not data.get(field):
            return False, "❗ Completa todos los campos."

    if data["source"] == data["dest"]:
        return False, "🚫 Origen y destino no pueden ser iguales."
    if data["duration"] <= 0:
        return False, "⏱️ Duración inválida."
    if data["days_left"] < 0:
        return False, "📆 Días restantes no pueden ser negativos."

    return True, ""


def transform_input(data, encoders, scaler, model_columns):
    """Transforma los inputs categóricos y numéricos para el modelo."""
    try:
        input_data = {
            "airline": encoders["airline"].transform([data["airline"]])[0],
            "flight": 0,
            "source_city": encoders["source_city"].transform([data["source"]])[0],
            "departure_time": encoders["departure_time"].transform([data["dep_time"]])[
                0
            ],
            "stops": encoders["stops"].transform([data["stops"]])[0],
            "arrival_time": encoders["arrival_time"].transform([data["arr_time"]])[0],
            "destination_city": encoders["destination_city"].transform([data["dest"]])[
                0
            ],
            "class": encoders["class"].transform([data["class_type"]])[0],
            "duration": float(data["duration"]),
            "days_left": int(data["days_left"]),
        }
        input_df = pd.DataFrame([input_data], columns=model_columns)
        return scaler.transform(input_df)
    except Exception as e:
        raise ValueError(f"Error en transformación: {str(e)}")


def get_top_10_importances(model, feature_names):
    importances = model.feature_importances_
    df_importances = pd.DataFrame({"feature": feature_names, "importance": importances})
    df_importances = df_importances.sort_values(by="importance", ascending=False).head(
        10
    )
    return df_importances
