from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class Item(BaseModel):
   name: str
   item_id: int

items_db={}
@app.post("/items/{items_id}")
async def custom_responses(item_id:Item):
   if item_id  not in Item:
      raise HTTPException(status_code=200,detail='post created')
   return {Exception}