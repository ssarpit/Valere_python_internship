from fastapi import FastAPI,BackgroundTasks
app=FastAPI()

def write_log(message:str):
    with open("log.txt","a") as f:
        f.write(f"{message} is ")

@app.get("/order/")
async def place_order(background_task:BackgroundTasks):
    background_task.add_task(write_log,"New order placed ")
    return {"message":"Your order is placed Successfully"}