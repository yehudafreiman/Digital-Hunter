from pymongo import MongoClient
import os

client = MongoClient(os.getenv('MONGO_URI', 'mongodb://mongodb:27017/'))
db = client["my_db"]
collection = db["myTable"]



