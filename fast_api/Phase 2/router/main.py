from fastapi import FastAPI
from routes import user,item
app=FastAPI()

app.include_router(user.router,prefix='/users',tags=["Users"])
app.include_router(item.router,prefix='/item',tags=['Item'])
