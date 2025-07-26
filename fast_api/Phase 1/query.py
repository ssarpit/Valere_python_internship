from fastapi import FastAPI
app=FastAPI()
@app.get('/user/{id}')
def show(id: int):
    return {'data':id}
@app.get('/user/{id}/comments')
def com(id:int ,limit=10):
    return {f'{limit} blogs are here' }

@app.get('/user/{id}/comments')
def comments(id):
    return {'data':{1,2}}

