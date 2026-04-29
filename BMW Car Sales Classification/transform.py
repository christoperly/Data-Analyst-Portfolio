import pandas as pd 
import requests
from datetime import datetime
from pyspark.sql import SparkSession

# Spark Session
spark = SparkSession.builder \
        .appName('BMW_Sales_Pipeline') \
        .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

# baca file CSV dari Folder Data
df = spark.read.csv('/opt/airflow/data/BMW_Car_Sales_Classification.csv', header=True, inferSchema=True)

# Tranfrom
# ubah nama menjadi lowercase
df = df.toDF(*[col.lower() for col in df.columns])

# hapus dulikat
df = df.dropDuplicates()

# hapus baris yg nilai nya kosong
df = df.dropna()

# simpan hasil tranfrom
df.toPandas().to_csv('/opt/airflow/data/transformed_BMW_Car_Sales_Classification.csv', index=False)

