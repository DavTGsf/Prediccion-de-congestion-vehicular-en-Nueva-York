import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import glob

# LOAD LOCAL EXPORTS

preds = pd.read_csv("/home/usuario/resultados_locales/predicciones.csv")
hour = pd.read_csv("/home/usario/resultados_locales/hour.csv")
boro = pd.read_csv("/home/usuario/resultados_locales/boro.csv")
error = pd.read_csv("/home/usuario/resultados_locales/error.csv")

# limpiar headers duplicados
hour = hour[hour["HH"] != "HH"]
boro = boro[boro["Boro"] != "Boro"]
error = error[error["label"] != "label"]

# convertir tipos
hour["HH"] = pd.to_numeric(hour["HH"])
hour["vol_real"] = pd.to_numeric(hour["vol_real"])
hour["vol_pred"] = pd.to_numeric(hour["vol_pred"])

error["label"] = pd.to_numeric(error["label"])
error["prediction"] = pd.to_numeric(error["prediction"])


# REAL VS PRED

plt.figure()
plt.scatter(error["label"], error["prediction"], alpha=0.3)
plt.savefig("real_vs_pred.png")


# ERROR HIST

plt.figure()
plt.hist(error["label"] - error["prediction"], bins=50)
plt.savefig("error_hist.png")


# HOUR

plt.figure()
plt.plot(hour["HH"], hour["vol_real"])
plt.plot(hour["HH"], hour["vol_pred"])
plt.savefig("trafico_hora.png")


# BOROUGH

plt.figure()
plt.bar(boro["Boro"], boro["vol_real"])
plt.savefig("trafico_boro.png")

print(" Visualizaciones generadas")
