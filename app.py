import dash
from dash import  Input, Output, State
from model_loader import load_model_and_dependencies
from layout import create_layout
from graphics import generate_graphs

model, scaler, categories, model_columns, test_data, metrics = (
    load_model_and_dependencies()
)
# Inicializar app
app = dash.Dash(__name__)
app.title = "Predicción de Vuelos"
server = app.server  

graphics = generate_graphs(
    test_data=test_data, model=model, feature_names=model_columns
)

app.layout = create_layout(
    airlines=categories["airlines"],
    cities=categories["cities"],
    times=categories["times"],
    classes=categories["classes"],
    stops=categories["stops"],
    graphic1=graphics["Precio Real vs Precio Predicho"],
    graphic2=graphics["Distribución de los Residuos"],
    graphic3=graphics["Top 10 Características"],
    metrics=metrics,
)


# callback
@app.callback(
    Output("output-prediction", "children"),
    Input("btn-predict", "n_clicks"),
    State("airline", "value"),
    State("source", "value"),
    State("dest", "value"),
    State("class", "value"),
    State("dep_time", "value"),
    State("arr_time", "value"),
    State("stops", "value"),
    State("duration", "value"),
    State("days_left", "value"),
)
def predict(
    n_clicks,
    airline,
    source,
    dest,
    class_type,
    dep_time,
    arr_time,
    stops,
    duration,
    days_left,
):

    if not n_clicks:
        return "📝 Ingresa los datos para predecir el precio."

    from utils import validate_inputs, transform_input

    input_data = {
        "airline": airline,
        "source": source,
        "dest": dest,
        "class_type": class_type,
        "dep_time": dep_time,
        "arr_time": arr_time,
        "stops": stops,
        "duration": duration,
        "days_left": days_left,
    }
    is_valid, message = validate_inputs(input_data)
    if not is_valid:
        return message

    try:
        transformed_input = transform_input(
            input_data, categories["encoders"], scaler, model_columns
        )
        pred = model.predict(transformed_input)[0]
        usd_price = pred / 86.5
        return f"💰 Precio estimado: ${usd_price:,.2f} USD"
    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=False)
