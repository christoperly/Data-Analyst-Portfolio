import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from pymongo import MongoClient

# baca hasil tranfrom.py
df = pd.read_csv('/opt/airflow/data/transformed_BMW_Car_Sales_Classification.csv')

#koneksi ke MongoDB Atlas
mongo_uri  = 'mongodb+srv://admin:admin@cluster0.nrcojq6.mongodb.net/?appName=Cluster0'
client = MongoClient(mongo_uri)

# database
db = client['bmw_sales_db']
collection = db['bmw_car_sales']

data = df.to_dict(orient='records')
collection.delete_many({})

# simpan ke MongoDB
collection.insert_many(data)

