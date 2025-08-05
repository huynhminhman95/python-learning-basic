
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://adminmongo:adminmongo@witty-coder.xtinj0o.mongodb.net/?retryWrites=true&w=majority&appName=witty-coder"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Truy cập database và collection
db = client['sample_mflix']
collection = db['movies']

# Send a ping to confirm a successful connection
try:
   #  client.admin.command('ping')
   #  print("Pinged your deployment. You successfully connected to MongoDB!")
   # Lấy 5 document đầu tiên
   #Query for a movie that has the title 'Back to the Future'
   query = { "title": "Back to the Future" }
   movie = collection.find_one(query)
   print(movie)
except Exception as e:
    print(e)