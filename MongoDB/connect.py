from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# connect mongoDB local
client = MongoClient("mongodb://localhost:27017/")

try:
   # Send handle ping
   client.admin.command("ping")
   print("MongoDB is runing and connected")
except ConnectionFailure:
   print("Can't connect MongoDB! Check server MongoDB is running!")


#

