
from fastapi import APIRouter
router=APIRouter()

@router.get('/')
def get_users():
    return [{'id':1,'name':"arpit"},{'id':2,"name":"Bob"}]
@router.get("/{user_id}")
def get_user(user_id:int):
    return [{'id':user_id,'name':'User Name'}]


