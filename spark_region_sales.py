from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import FloatType
from pyspark.sql.functions import sum as sm

# Create a SparkSession
spark = SparkSession.builder \
    .appName("CSV Loader") \
    .getOrCreate()
    
    
    
df = spark.read.csv(r"Data\region_sales.csv", header=True, inferSchema=True)
df.show(10)



# Replace non-numeric values with null and cast to float
df_clean = df.withColumn(
    "value_num",
    when(
        (col("sales").rlike("^[+-]?([0-9]*[.])?[0-9]+$")) & (col("sales") != "NaN"),
        col("sales").cast(FloatType())
    ).otherwise(None)
)

df_clean.show(10)



df_clean.select(sm("value_num").alias("total_sales")).show()