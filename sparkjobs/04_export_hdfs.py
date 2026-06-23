predictions = spark.read.parquet("hdfs://localhost:9000/trafico/resultados/rf_predictions")

predictions.select("Borough", "HH", "label", "prediction") \
    .write.mode("overwrite") \
    .csv("hdfs://localhost:9000/trafico/resultados/predicciones_csv")

df_hour.write.mode("overwrite").csv(
    "hdfs://localhost:9000/trafico/resultados/hour_stats", header=True)

df_boro.write.mode("overwrite").csv(
    "hdfs://localhost:9000/trafico/resultados/boro_stats", header=True)

df_error.write.mode("overwrite").csv(
    "hdfs://localhost:9000/trafico/resultados/error_stats", header=True)
