# model_loader.py
import joblib


def load_model_and_dependencies():
    # Cargar todo el diccionario con los objetos
    data = joblib.load("modelo_vuelos_completo.pkl")

    model = data["model"]
    scaler = data["scaler"]
    encoders = data["label_encoders"]
    test_data = data["test_data"]
    model_columns = data["model_columns"]
    metrics = data["result_metrics"]

    # Extraer categorías para usar en dropdowns
    categories = {
        "airlines": encoders["airline"].classes_.tolist(),
        "cities": encoders["source_city"].classes_.tolist(),
        "times": encoders["departure_time"].classes_.tolist(),
        "classes": encoders["class"].classes_.tolist(),
        "stops": encoders["stops"].classes_.tolist(),
        "encoders": encoders,
    }
    return model, scaler, categories, model_columns, test_data, metrics
