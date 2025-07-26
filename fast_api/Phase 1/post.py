from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
class Blog(BaseModel):
    name:str
    title:str
    published: Optional[bool]
app=FastAPI()

@app.post("/user")

def create_user(request:Blog):
    return {'data' :f"{request.title} is created"}