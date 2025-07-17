from bson import ObjectId
from fastapi import FastAPI, APIRouter, HTTPException
from MongoDB.config import collection
from MongoDB.database.schemas import all_tasks
from MongoDB.database.models import Todo
from datetime import datetime

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_todos():
   data = collection.find({"is_deleted":False})
   return all_tasks(data)

@router.post("/")
async def create_teask(new_task: Todo):
   try:
      resp = collection.insert_one(new_task.model_dump())
      return {"status_code":200, "id":str(resp.inserted_id)}
   except Exception as e:
      return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.put("/{task_id}")
async def update_tasks(task_id:str, update_tasks:Todo):
   try:
      id = ObjectId(task_id)
      exesting_doc = collection.find_one({"_id":id, "is_deleted":False})
      if not exesting_doc:
         return HTTPException(status_code=404, detail=f"Task does not exits")
      update_tasks.updated_at = int(datetime.timestamp(datetime.now()))
      resp = collection.update_one({"_id":id}, {"$set":dict(update_tasks)})
      return {"status_code":200, "message":"Task update successfully"}
   except Exception as e:
      return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.delete("/{task_id}")
async def delete_task(task_id:str):
   try:
      id = ObjectId(task_id)
      exesting_doc = collection.find_one({"_id":id, "is_deleted":False})
      if not exesting_doc:
         return HTTPException(status_code=404, detail=f"Task does not exits")
      resp = collection.update_one({"_id":id}, {"$set":{"is_deleted":True}})
      return {"status_code":200, "message":"Task deleted successfully"}
   except Exception as e:
      return HTTPException(status_code=500, detail=f"Some error occured {e}")

app.include_router(router)