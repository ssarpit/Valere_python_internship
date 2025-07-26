from fastapi import FastAPI,Depends,HTTPException

app=FastAPI()

def verify_token(token:str=""):
    if token!='secret123':
        raise HTTPException(status_code=404,detail='Token is invalid')
    return token

@app.get("/secure_data")
def get_user(token:str=Depends(verify_token)):
    return {'message':'Token Verified'}
