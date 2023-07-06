import json

from pymongo import MongoClient
from _datetime import datetime
from models import Authors, Quotes
from connect import user, password, domain, db_name

client = MongoClient(f"mongodb+srv://{user}:{password}@{domain}/{db_name}?retryWrites=true&w=majority")

db = client.hw_eight_db
result = db.authors.insert_many(Authors)
result_get = db.authors.find({})
[print(el) for el in result_get]