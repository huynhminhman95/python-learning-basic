from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# connect mongoDB local
client = MongoClient("mongodb://localhost:27017/")

# create or choose database
db = client["company"]
employees = db["employees"]

# NOTE: group by and count total employee
# pipeline = [
#    {"$group": {"_id": "$position", "total": {"$sum" : 1}}}
# ]
# for result in employees.aggregate(pipeline):
#    print(result)

# NOTE: filters, sort, group
pipeline = [
   {
      "$match":{
         "age": {"$gt": 25}
      }
   },
   {
      "$group":{
         "_id": "$position",
         "total": {"$sum": 1}
      }
   },
   {
      "$sort":{
         "total": -1
      }
   }
]

# for result in employees.aggregate(pipeline):
#    print(result)

# NOTE: create index
# employees.create_index([("name", 1)])
# indexes = employees.list_indexes()
# for emp in indexes:
#    print(emp)

index_names = employees.index_information()
for name, info in index_names.items():
    print(f"Index name: {name}, Fields: {info['key']}")
