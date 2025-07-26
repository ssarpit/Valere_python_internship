from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse

app=FastAPI()
@app.exception_handler(404)
def custom_404_error_handler(request: Request, exc: HTTPException):
    print("404 handler triggered")
    return JSONResponse(
        status_code=404,
        content={"error": "The resource not found"}
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    print("HTTPException handler triggered")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": f"Oops! {exc.detail}"}
    )

@app.get("/item/{item_id}")
async def item_exception(item_id:int):
   if item_id==0:
      raise HTTPException(status_code=400,detail="Invalid item id")
   return {"item_id":item_id}
