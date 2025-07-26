from fastapi import FastAPI,Request
import time
app=FastAPI()

@app.middleware('http')

async def timer(request:Request,call_next):
    start_time=time.time()
    response=await call_next(Request)
    process_time=time.time()-start_time
    response.headers["X-Process_time"]=str(process_time)
    return response

@app.get('/')
async def raw():
    return {'message':'process_time'}