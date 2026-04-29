import requests
from datetime import datetime
import pandas as pd
import os
from pyspark.sql import SparkSession

# Spark Session
spark = SparkSession.builder \
        .appName('BMW_Sales_Pipeline') \
        .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

# baca file CSV dari Folder Data
df = spark.read.csv('/opt/airflow/data/BMW_Car_Sales_Classification.csv', header=True, inferSchema=True)
