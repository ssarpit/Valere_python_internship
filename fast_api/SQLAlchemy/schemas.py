from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    name:str
    email:EmailStr

class Userread(UserCreate):
    id:int 
    
    class Config:
        orm_mode=True

