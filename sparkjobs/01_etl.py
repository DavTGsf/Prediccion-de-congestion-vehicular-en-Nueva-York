from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("ETL").getOrCreate()

df = spark.read.csv("hdfs://localhost:9000/trafico/raw/trafico.csv", header=True)

df = df.dropna()

df = df.withColumn(
    "rush_hour",
    ((col("HH") >= 7) & (col("HH") <= 9)) | ((col("HH") >= 16) & (col("HH") <= 18))
)

df.write.mode("overwrite").parquet("hdfs://localhost:9000/trafico/processed/data")
