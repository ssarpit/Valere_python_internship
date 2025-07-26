from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class AnimatedCuisines(str,Enum):
    indian="indian"
    american="american"

food_items={
    'indian':['samosa','kachori'],
    'american':['hot dog','apple pie']
}


@app.get("/get_items/{item_id}")
async def read_item(item_id: AnimatedCuisines):
    return food_items.get(item_id)