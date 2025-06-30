from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# connect mongoDB local
client = MongoClient("mongodb://localhost:27017/")

# create or choose database
db = client["company"]
employees = db["employees"]

#  giam dan
for emp in employees.find().sort("age", -1):
   print(emp)

print("--------")
# limit
for emp in employees.find().sort("age", -1).limit(2):
   print(emp)

print("--------")
# count document
count = employees.count_documents({})
print("Total employees: ", count)