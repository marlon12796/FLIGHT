# layout.py
from dash import html, dcc


def create_layout(
    airlines, cities, times, classes, stops, graphic1, graphic2, graphic3, metrics
):
    return html.Div(
        [
            html.Header(
                [html.H1("✈️ Predicción de Precio de Vuelos", className="app-title")],
                className="header",
            ),
            html.Main(
                [
                    html.Section(
                        [
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id="airline",
                                        options=[
                                            {"label": f"🛫 {i}", "value": i}
                                            for i in airlines
                                        ],
                                        placeholder="Selecciona Aerolínea",
                                        className="input-field",
                                    ),
                                    dcc.Dropdown(
                                        id="class",
                                        options=[
                                            {"label": f"💺 {i}", "value": i}
                                            for i in classes
                                        ],
                                        placeholder="Clase",
                                        className="input-field",
                                    ),
                                    dcc.Dropdown(
                                        id="source",
                                        options=[
                                            {"label": f"📍 {i}", "value": i}
                                            for i in cities
                                        ],
                                        placeholder="Ciudad de Origen",
                                        className="input-field",
                                    ),
                                    dcc.Dropdown(
                                        id="dest",
                                        options=[
                                            {"label": f"🎯 {i}", "value": i}
                                            for i in cities
                                        ],
                                        placeholder="Destino",
                                        className="input-field",
                                    ),
                                    dcc.Dropdown(
                                        id="dep_time",
                                        options=[
                                            {"label": f"🕕 {i}", "value": i}
                                            for i in times
                                        ],
                                        placeholder="Hora de Salida",
                                        className="input-field",
                                    ),
                                    dcc.Dropdown(
                                        id="arr_time",
                                        options=[
                                            {"label": f"🕗 {i}", "value": i}
                                            for i in times
                                        ],
                                        placeholder="Hora de Llegada",
                                        className="input-field",
                                    ),
                                    dcc.Dropdown(
                                        id="stops",
                                        options=[
                                            {"label": f"🔁 {i}", "value": i}
                                            for i in stops
                                        ],
                                        placeholder="Escalas",
                                        className="input-field",
                                    ),
                                    html.Div(
                                        [
                                            dcc.Input(
                                                id="duration",
                                                type="number",
                                                placeholder="⏱️ Duración (horas)",
                                                className="input-field",
                                            )
                                        ],
                                        className="container-field",
                                    ),
                                    html.Div(
                                        [
                                            dcc.Input(
                                                id="days_left",
                                                type="number",
                                                placeholder="📆 Días restantes",
                                                className="input-field",
                                            )
                                        ],
                                        className="container-field",
                                    ),
                                ],
                                className="grid-container",
                            ),
                            html.Div(
                                [
                                    html.Button(
                                        "🔍 Predecir Precio",
                                        id="btn-predict",
                                        n_clicks=0,
                                        className="btn-primary",
                                    )
                                ],
                                className="btn-container",
                            ),
                            html.H3(id="output-prediction", className="output-box"),
                        ],
                        className="card",
                    ),
                    html.Section(
                        [
                            html.H2("Dashboard", className="graph-section__title"),
                            html.Div(
                                [
                                    html.Div(
                                        dcc.Graph(figure=graphic1),
                                        className="graph-container",
                                    ),
                                    html.Div(
                                        dcc.Graph(figure=graphic2),
                                        className="graph-container",
                                    ),
                                    html.Div(
                                        dcc.Graph(figure=graphic3),
                                        className="graph-container",
                                    ),
                                    html.Ul(
                                        [
                                            html.Li(
                                                [
                                                    html.P(
                                                        "R²:", className="metric-label"
                                                    ),
                                                    html.P(
                                                        f"{metrics['R2_score']:.4f}",
                                                        className="metric-value",
                                                    ),
                                                ],
                                                className="metric-box",
                                            ),
                                            html.Li(
                                                [
                                                    html.P(
                                                        "RMSE:",
                                                        className="metric-label",
                                                    ),
                                                    html.P(
                                                        f"{metrics['Root_Mean_Squared_Error_RMSE']:.2f}",
                                                        className="metric-value",
                                                    ),
                                                ],
                                                className="metric-box",
                                            ),
                                            html.Li(
                                                [
                                                    html.P(
                                                        "MAE:", className="metric-label"
                                                    ),
                                                    html.P(
                                                        f"{metrics['Mean_Absolute_Error_MAE']:.2f}",
                                                        className="metric-value",
                                                    ),
                                                ],
                                                className="metric-box",
                                            ),
                                            html.Li(
                                                [
                                                    html.P(
                                                        "MAPE:",
                                                        className="metric-label",
                                                    ),
                                                    html.P(
                                                        f"{metrics['Mean_Absolute_Percentage_Error_MAPE']:.2f}%",
                                                        className="metric-value",
                                                    ),
                                                ],
                                                className="metric-box",
                                            ),
                                            html.Li(
                                                [
                                                    html.P(
                                                        "Adj R²:",
                                                        className="metric-label",
                                                    ),
                                                    html.P(
                                                        f"{metrics['Adj_R_Square']:.4f}",
                                                        className="metric-value",
                                                    ),
                                                ],
                                                className="metric-box",
                                            ),
                                        ],
                                        className="graph-container",
                                    ),
                                ],
                                className="graph-content",
                            ),
                        ],
                        className="graph-section",
                    ),
                ],
                className="main",
            ),
        ],
        className="page",
    )
