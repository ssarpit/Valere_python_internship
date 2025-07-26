from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

user_db=[]

class User(BaseModel):
    id:int
    name:str|None

class UserUpdate(BaseModel):
    name:str

@app.post("/user")
def create_user(user:User):
    user_db.append(user)
    return user_db

@app.get("/users/{user_id}")
def get_user(user_id:int):
    for user in user_db:
        if user.id==user_id:
            return user
    raise HTTPException(status_code=404,detail='user not found')

@app.put('/users/{user_id}')

def update_user(user_id:int,updated_user:UserUpdate):
    for user in user_db:
        if user.id==user_id:
            user.name=updated_user.name
            return user
    raise HTTPException(status_code=201,detail='user is not available in db')

@app.delete('/users/{user_id}')
def delete_user(user_id:int):
    for user in user_db:
        if user.id==user_id:
            user_db.remove(user)
            return {'message':"User deleted"}
    raise HTTPException(status_code=204,detail='No user')