from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# connect mongoDB local
client = MongoClient("mongodb://localhost:27017/")

# create or choose database
db = client["company"]
employees = db["employees"]

# NOTE: insert one document
employee = {"name":"Minh", "age":30, "position":"Developer"}
# result = employees.insert_one(employee)
# print("Da insert voi _id:", result.inserted_id)

# NOTE: insert multiple document
employee_list = [
   {"name":"Tung", "age":32, "position":"Electronic"},
   {"name":"Truong", "age":28, "position":"Inverter"}
]
# result = employees.insert_many(employee_list)
# print("Da insert nhieu document: ", result.inserted_ids)

# NOTE: read document
for emp in employees.find():
   print(emp)

# NOTE: filter theo dieu kien
print("------")
filter = {"position":"Developer"}
for emp in employees.find(filter):
   print(emp)

# NOTE: find one employee
print("------")
filter = {"name":"Chi"}
for emp in employees.find(filter):
   print(emp)

# NOTE: Choose field projection
print("------")
filter = {"position":1, "_id":0}
for emp in employees.find({}, filter):
   print(emp)