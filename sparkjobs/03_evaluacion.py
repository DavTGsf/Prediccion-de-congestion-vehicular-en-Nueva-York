from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator

spark = SparkSession.builder.appName("eval").getOrCreate()

predictions = spark.read.parquet(
    "hdfs://localhost:9000/trafico/resultados/rf_predictions"
)

rmse_eval = RegressionEvaluator(labelCol="label", predictionCol="prediction", metricName="rmse")
mae_eval = RegressionEvaluator(labelCol="label", predictionCol="prediction", metricName="mae")
r2_eval = RegressionEvaluator(labelCol="label", predictionCol="prediction", metricName="r2")

rmse = rmse_eval.evaluate(predictions)
mae = mae_eval.evaluate(predictions)
r2 = r2_eval.evaluate(predictions)

print("RMSE:", rmse)
print("MAE:", mae)
print("R2:", r2)
