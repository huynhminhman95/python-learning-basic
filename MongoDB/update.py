from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# connect mongoDB local
client = MongoClient("mongodb://localhost:27017/")

# create or choose database
db = client["company"]
employees = db["employees"]

# NOTE: update one document
# result = employees.update_one(
#    {"name":"Minh"},
#    {"$set":{"age": 28}}
# )
# print("So document duoc cap nhat: ", result.modified_count)

# NOTE: update multiple document
# result = employees.update_many(
#    {"position":"Developer"},
#    {"$set":{"level":"Junior"}}
# )
# print("So document updated: ", result.modified_count)
for emp in employees.find():
   print(emp)