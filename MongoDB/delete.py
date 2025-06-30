from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# connect mongoDB local
client = MongoClient("mongodb://localhost:27017/")

# create or choose database
db = client["company"]
employees = db["employees"]

# NOTE: delete one document
# result = employees.delete_one({"name":"Man"})
# print("Document bi xoa: ", result.deleted_count)

# NOTE: delete multiple document
# result = employees.delete_many({"position":"Developer"})
# print("Document bi xoa: ", result.deleted_count)
for emp in employees.find():
   print(emp)