# app/main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from .api.endpoints import auth, contests, challenges, submissions
from .services.leaderboard_manager import manager
from .db.database import engine
from .db import models

# Create database tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Coding Contest Platform ")

# Include API routers from the endpoints
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(contests.router, prefix="/contests", tags=["Contests"])
app.include_router(challenges.router, prefix="/challenges", tags=["Challenges"])
app.include_router(submissions.router, prefix="/submissions", tags=["Submissions"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the  Coding Contest Platform "}

@app.websocket("/ws/leaderboard/{contest_id}")
async def websocket_endpoint(websocket: WebSocket, contest_id: int):
    """
    WebSocket endpoint for the real-time leaderboard.
    """
    await manager.connect(websocket, contest_id)
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive
    except WebSocketDisconnect:
        manager.disconnect(websocket, contest_id)