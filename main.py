import pymongo
import json

from pymongo import MongoClient
from bson.objectid import ObjectId

try:
    conn = MongoClient("mongodb+srv://altcointraders:rrxRhjvyUEPltaGC@at.u2irqhk.mongodb.net")
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")

dblist = conn.list_database_names()
for db in dblist:
   print(db)

if "learning" in dblist:
  print("The database exists.")


db = conn.learning

collectionNames = db.list_collection_names()
if "document" in collectionNames:
  print("The collection exists.")

documents=db.document

doc= {
    'title': 'MongoDB and Python', 
    'description': 'MongoDB is no SQL database', 
    'tags': ['mongodb', 'database', 'NoSQL'], 
    'viewers': 104 
}

documents.insert_one(doc)

for db in documents.find({'title': 'MongoDB and Python'}):
    print(db)

for doc in documents.find():
    print(doc['_id'])

