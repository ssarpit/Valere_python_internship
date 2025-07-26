from model import create_table
from sqlalchemy import engine
from services import *
from router import router
#Create tables
from fastapi import FastAPI
from db import SessionLocal 

app=FastAPI()
create_table()
db: Session=SessionLocal()
# create_user(db,"iamaj","iamaj0275@gmail.com")
create_user(db,"arpit","arpit05@gmail.com")
# create_user(db,"ajarpit","all@gmail.com")
# create_user(db,"kon","con12@gmail")



# print(get_single_user(1))
#Getting all user data
# print(get_users())
# print(update_data(2,"arpitofficial0206@gmail.com"))
# delete_data(7)
# delete_all_users()

app.include_router(router)