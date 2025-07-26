from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins=[
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_credentials=True,
    allow_headers=["*"],
)

@app.get('/')
def check():
    return {'message':"CORS DONE"}