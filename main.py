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

# if "learning" in dblist:
#   print("The database exists.")


db = conn.learning

# collectionNames = db.list_collection_names()
# if "document" in collectionNames:
#   print("The collection exists.")

documents=db.document

doc= {
    '_id': ObjectId('645fa85e2dad47c704f83e00'),
    'title': 'MongoDB and Python2', 
    'description': 'MongoDB is no SQL database', 
    'tags': ['mongodb', 'database', 'NoSQL'], 
    'viewers': 104 
}
try:
    documents.insert_one(doc)
except pymongo.errors.DuplicateKeyError :    
    print('document already exists')

customers = db.customers

mylist= [
 { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = customers.insert_many(mylist)
print(x.inserted_ids)


# for db in documents.find({'title': 'MongoDB and Python'}):
#     print(db)

# for doc in documents.find():
#     print(doc['_id'])

