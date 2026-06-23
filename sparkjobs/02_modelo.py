from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor

spark = SparkSession.builder.appName("modelo").getOrCreate()

df = spark.read.parquet("hdfs://localhost:9000/trafico/processed/data")

assembler = VectorAssembler(inputCols=["HH", "rush_hour"], outputCol="features")
df = assembler.transform(df).withColumnRenamed("Vol", "label")

train, test = df.randomSplit([0.8, 0.2])

rf = RandomForestRegressor(featuresCol="features", labelCol="label")
model = rf.fit(train)

predictions = model.transform(test)

predictions.write.mode("overwrite") \
    .parquet("hdfs://localhost:9000/trafico/resultados/rf_predictions")
