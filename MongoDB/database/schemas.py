def individual_data(todo):
   return {
      "id": str(todo["_id"]),
      "title": todo["title"],
      "description": todo["description"],
      "status": todo["is_completed"],
      "deleted": todo["is_deleted"]
   }

def all_tasks(todos):
   return [individual_data(todo) for todo in todos]