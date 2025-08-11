import pandas as pd
import plotly.express as px
from utils import get_top_10_importances


def fn_scatter_pred(df_pred=pd.DataFrame):
    fig_scatter = px.scatter(
        df_pred,
        x="Precio Real",
        y="Precio Predicho",
        title="📊 Precio Real vs Precio Predicho",
        opacity=0.8,
        labels={"Precio Real": "Precio Real", "Precio Predicho": "Precio Predicho"},
        color="Precio Real",  # Color gradual según precio real
        color_continuous_scale="Viridis",
        size_max=8,
    )
    fig_scatter.add_shape(
        type="line",
        x0=df_pred["Precio Real"].min(),
        y0=df_pred["Precio Real"].min(),
        x1=df_pred["Precio Real"].max(),
        y1=df_pred["Precio Real"].max(),
        line=dict(color="red", dash="dash"),
        name="Línea Ideal",
    )
    fig_scatter.update_layout(
        template="plotly_dark",  # 👈 Este es el truco: tema oscuro
        title_font_size=20,
        font_color="white",
        paper_bgcolor="#13161b",  # Fondo del gráfico
        plot_bgcolor="#0e1117",  # Fondo del área de trazado
        hovermode="closest",
        margin=dict(l=50, r=50, t=60, b=50),
    )
    return fig_scatter


def fn_hist_errors(df_pred=pd.DataFrame):
    residuos = df_pred["Precio Real"] - df_pred["Precio Predicho"]
    df_resid = pd.DataFrame({"Residuo": residuos})
    fig_hist = px.histogram(
        df_resid,
        x="Residuo",
        nbins=30,
        title="Distribución de los Residuos",
        labels={"Residuo": "Error (Real - Predicho)"},
        opacity=0.8,
        color_discrete_sequence=["salmon"],
        marginal=None,  # No mostrar boxplot o rugplot
        histnorm="density",  # Normaliza para que el área total sea 1 (útil para superponer KDE)
    )

    # Estilo oscuro
    fig_hist.update_layout(
        template="plotly_dark",
        title_font_size=20,
        font_color="white",
        paper_bgcolor="#13161b",
        plot_bgcolor="#0e1117",
        xaxis_title="Error (Real - Predicho)",
        yaxis_title="Densidad / Frecuencia",
        bargap=0.1,
    )
    return fig_hist


import plotly.express as px


def fn_bar_top10_importances(df_importances=pd.DataFrame):
    fig_bar = px.bar(
        df_importances,
        x="importance",
        y="feature",
        orientation="h",
        title="Top 10 Características Más Importantes",
        labels={"importance": "Importancia", "feature": "Características"},
        color="importance",
        color_continuous_scale=["#2ECC71", "#F1C40F", "#E74C3C"],
        text="importance",
    )
    fig_bar.update_layout(
        template="plotly_dark",
        title_font_size=20,
        font_color="white",
        paper_bgcolor="#13161b",
        plot_bgcolor="#0e1117",
        yaxis=dict(autorange="reversed"),
        margin=dict(l=80, r=40, t=100, b=60),
        autosize=True,
        coloraxis_showscale=False,
        width=None,
    )
    fig_bar.update_traces(
        texttemplate="%{text:.1%}",
        textposition="outside",
    )
    return fig_bar


def generate_graphs(test_data, model, feature_names):
    df_importances_10 = get_top_10_importances(model=model, feature_names=feature_names)
    df_pred = pd.DataFrame(
        {
            "Precio Real": test_data["y_test"],
            "Precio Predicho": test_data["y_pred"],
        }
    )
    scatter_figure = fn_scatter_pred(df_pred=df_pred)
    error_hist_figure = fn_hist_errors(df_pred=df_pred)
    top10_figure = fn_bar_top10_importances(df_importances=df_importances_10)
    return {
        "Precio Real vs Precio Predicho": scatter_figure,
        "Distribución de los Residuos": error_hist_figure,
        "Top 10 Características": top10_figure,
    }
