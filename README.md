# ✈️ Flight Price Prediction App  

Aplicación web interactiva desarrollada con **Dash (Plotly)** para predecir precios de vuelos en India.  
El modelo de Machine Learning se entrenó con un **RandomForestRegressor**, alcanzando un **R² de 0.983** sobre el conjunto de prueba.  

La aplicación permite:  
- 🔮 Predecir precios de vuelos en base a aerolínea, ciudad, clase, duración, escalas, días de anticipación, etc.  
- 📊 Visualizar métricas del modelo y gráficos interactivos.  
- ⚡ Explorar la importancia de las características en la predicción de precios.  

---

## 📂 Dataset  

El dataset proviene de **EaseMyTrip**, con **300,261 registros** y **11 características**.  
- **Periodo de recolección:** 11 Feb – 31 Mar 2022.  
- **Ciudades:** 6 principales ciudades de India.  
- **Clases:** Economy y Business.  

**Características principales:**  
- `Airline` – Nombre de la aerolínea.  
- `Source City` – Ciudad de origen.  
- `Destination City` – Ciudad de destino.  
- `Departure Time / Arrival Time` – Intervalos categorizados de horarios.  
- `Stops` – Número de escalas.  
- `Duration` – Duración total del vuelo (horas).  
- `Days Left` – Días de anticipación en la compra.  
- `Class` – Economy o Business.  
- `Price` – 🎯 Variable objetivo.  

---

## 🧠 Modelo  

- Algoritmo: **RandomForestRegressor**  
- Métricas de evaluación:  

| Métrica | Valor |
|---------|-------|
| R²      | 0.983 |
| MAE     | 1425.16 |
| RMSE    | 2938.37 |
| MAPE    | 10.92% |

---

## 🖥️ App Dash  

La aplicación está construida con **Dash + Plotly**.  

### 📊 Visualizaciones incluidas:
- Precio Real vs Precio Predicho  
- Distribución de los Residuos  
- Top 10 Características más importantes  

### 📌 Flujo de la App:
1. El usuario selecciona **aerolínea, origen, destino, clase, horarios, duración, días de anticipación, escalas**.  
2. El input se valida y transforma con los mismos **encoders** y **scaler** usados en el entrenamiento.  
3. El modelo predice el precio y lo muestra en **USD**.  

---

## ⚙️ Instalación y Ejecución  

### 🔹 Clonar repositorio
```bash
git clone https://github.com/tuusuario/flight-price-prediction.git
cd flight-price-prediction
```

### 🔹 Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate   # en Linux/Mac
venv\Scripts\activate      # en Windows

pip install -r requirements.txt
```

### 🔹 Ejecutar la app
```bash
python app.py
```
La app estará disponible en: 👉 http://127.0.0.1:8050  

---

## 🚀 Futuras Mejoras  
- 🔗 Integrar API REST para exponer predicciones.  
- 📱 Hacer la app responsive con componentes Dash Bootstrap.  
---

## 📌 Créditos  
- Dataset: *EaseMyTrip (scrapeado con Octoparse)*  
- Autor: **MARLON**  
- Librerías: Dash, Plotly, Scikit-Learn, Pandas, Numpy  
