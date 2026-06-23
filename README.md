#  Predicción de congestión vehicular en Nueva York con Apache Spark

##  Overview

Este proyecto implementa un pipeline de Big Data utilizando **Apache Spark** para analizar y predecir el volumen de tráfico vehicular en distintas zonas urbanas de la ciudad de Nueva York.

El objetivo es transformar grandes volúmenes de datos de tráfico en información accionable mediante técnicas de **Data Engineering** y **Machine Learning**, permitiendo identificar patrones de congestión y generar predicciones precisas sobre el flujo vehicular.

La solución integra procesamiento distribuido con Spark, almacenamiento en HDFS y un modelo de regresión basado en **Random Forest Regressor** de Spark MLlib para estimar el volumen de tráfico en función de variables temporales y geográficas.

---

##  Problem Statement

La gestión eficiente de la movilidad urbana requiere comprender cómo varía el tráfico a lo largo del tiempo y entre diferentes zonas de una ciudad.

Los sistemas tradicionales de análisis presentan limitaciones al procesar grandes volúmenes de información generados por sensores y sistemas de monitoreo vial.

Este proyecto aborda el problema mediante un pipeline escalable capaz de:

* Procesar grandes volúmenes de datos de tráfico.
* Identificar patrones de congestión por hora y ubicación.
* Generar predicciones del volumen vehicular.
* Evaluar el desempeño del modelo mediante métricas estándar de regresión.
* Proporcionar visualizaciones para apoyar la toma de decisiones.

---

##  Dataset

### Fuente

NYC Open Data – Automated Traffic Volume Counts

https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt/about_data

### Variables utilizadas

| Variable  | Descripción                               |
| --------- | ----------------------------------------- |
| Borough   | Zona geográfica de la ciudad              |
| HH        | Hora del día                              |
| Vol       | Volumen de tráfico registrado             |
| Date      | Fecha de observación                      |
| Rush_Hour | Indicador de hora pico (feature derivada) |

### Características del dataset

* Datos históricos de tráfico vehicular.
* Cobertura de múltiples boroughs de Nueva York.
* Registros horarios.
* Adecuado para tareas de análisis exploratorio y predicción.

---

#  Pipeline

## 1. Data Ingestion

Los datos son descargados desde NYC Open Data e incorporados al ecosistema Hadoop mediante HDFS.

### Objetivos

* Centralizar el almacenamiento.
* Permitir procesamiento distribuido.
* Facilitar escalabilidad para grandes volúmenes de datos.

---

## 2. ETL con Apache Spark

Durante esta etapa se realiza:

### Extracción

Lectura de archivos CSV desde HDFS utilizando PySpark.

### Transformación

* Eliminación de registros inválidos.
* Tratamiento de valores nulos.
* Conversión de tipos de datos.
* Normalización de columnas relevantes.

### Carga

Persistencia de datasets limpios para etapas posteriores.

---

## 3. Feature Engineering

Se construyen variables derivadas para mejorar la capacidad predictiva del modelo.

### Features principales

* Hora del día (`HH`)
* Borough
* Indicador de hora pico (`Rush_Hour`)
* Variables categóricas codificadas


---

## 4. Model Training

Se utiliza un modelo de regresión basado en **Random Forest Regressor** implementado en Spark MLlib.

### Motivos de selección

* Manejo eficiente de relaciones no lineales.
* Robustez frente a ruido en los datos.
* Buen desempeño con variables mixtas.
* Escalabilidad en entornos distribuidos.

### Configuración general

```python
RandomForestRegressor(
    featuresCol="features",
    labelCol="traffic_volume",
    numTrees=100
)
```

---

## 5. Model Evaluation

El rendimiento se evalúa mediante métricas estándar de regresión.

### RMSE (Root Mean Squared Error)

Mide la magnitud promedio del error penalizando errores grandes.

```text
RMSE ↓ = Mejor
```

### MAE (Mean Absolute Error)

Mide la diferencia absoluta promedio entre valores reales y predichos.

```text
MAE ↓ = Mejor
```

### R² (Coefficient of Determination)

Indica qué proporción de la variabilidad es explicada por el modelo.

```text
R² ↑ = Mejor
```

---

## 6. Exportación de Resultados

Las predicciones generadas se almacenan nuevamente en HDFS para consumo posterior.

### Salidas generadas

* Dataset de predicciones.
* Métricas de evaluación.
* Datos agregados para visualización.

---

## 7. Visualización

Se utilizan **Pandas** y **Matplotlib** para construir gráficos exploratorios y de evaluación.

---

#  Model

## Algoritmo

**Random Forest Regressor**

Tipo:

```text
Supervised Machine Learning
Regression
```

### Variable objetivo

```text
Traffic Volume
```

### Variables predictoras

```text
- Borough
- HH
- Rush_Hour
- Features derivadas
```

---

#  Metrics

Las métricas calculadas durante la evaluación incluyen:

| Métrica | Descripción                  |
| ------- | ---------------------------- |
| RMSE    | Error cuadrático medio       |
| MAE     | Error absoluto medio         |
| R²      | Coeficiente de determinación |


---

#  Results

## 1. Tráfico por Hora

Análisis temporal del volumen vehicular.

Hallazgos esperados:

* Incremento significativo durante horas pico.
* Mayor congestión en la mañana y al final de la jornada laboral.
* Reducción del tráfico durante la madrugada.

---

## 2. Tráfico por Borough

Comparación del volumen promedio entre zonas.

Objetivos:

* Identificar áreas de mayor congestión.
* Detectar patrones geográficos relevantes.
* Priorizar zonas para planificación urbana.

---

## 3. Distribución del Error

Visualización de residuos:

```text
Error = Real - Predicción
```

Permite:

* Detectar sesgos.
* Evaluar estabilidad del modelo.
* Identificar valores atípicos.

---

## 4. Real vs Predicción

Gráfico de dispersión para comparar:

```text
Valor Real
vs
Valor Predicho
```

Un buen modelo mostrará puntos cercanos a la diagonal principal.

---

#  Estructura del Repositorio

```text
proyecto_trafico/
│
├── data/
│   ├── raw/
│       └── DATASET_SOURCE.md
│
├── spark_jobs/
│   ├── 01_etl.py
│   ├── 02_modelo.py
│   ├── 03_modelo.py
│   └── 04_export_hdfs.py
│
├── visualization/
│   └── 04_visualization.py
│
│
└── README.md
```

---

# How to Run

## 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/proyecto_trafico.git

cd proyecto_trafico
```

---

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 3. Iniciar Hadoop y Spark

```bash
start-dfs.sh

start-all.sh
```

Verificar servicios:

```bash
jps
```

---

## 4. Cargar datos en HDFS

```bash
hdfs dfs -mkdir -p /traffic/raw

hdfs dfs -put traffic.csv /traffic/raw/
```

---

## 5. Ejecutar ETL

```bash
spark-submit spark_jobs/etl.py
```

---

## 6. Ejecutar entrenamiento

```bash
spark-submit spark_jobs/train_model.py
```

---

## 7. Generar visualizaciones

```bash
python visualization/traffic_by_hour.py

python visualization/traffic_by_borough.py

python visualization/prediction_analysis.py
```

---

#  Requirements

```text
pyspark
pandas
matplotlib
numpy
```

---

### Tecnologías utilizadas

* Apache Spark (PySpark)
* Hadoop HDFS
* Spark MLlib
* Pandas
* Matplotlib

