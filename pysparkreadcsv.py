from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder \
    .appName("CSV Loader") \
    .getOrCreate()
    
    
    
df = spark.read.csv(r"Data\customers.csv", header=True, inferSchema=True)
df = df.withColumn("score", round(rand()*40+60))

df.printSchema()
df.select(
    sum("score").alias("total_score"),
    avg("score").alias("average_score")
).show()

#$df.show(10)


spark.stop()