from fastapi import APIRouter

router=APIRouter()

@router.get("/")
def list_items():
    return [{'id':'1','name':'ice'},{'id':'2','name':'cold'}]

@router.get("/item_id")
def get_items():
    return [{'id':'item_id','name':'Item name'}]

