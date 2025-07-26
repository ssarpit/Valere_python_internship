from fastapi import WebSocket
from typing import List, Dict

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, contest_id: int):
        await websocket.accept()
        if contest_id not in self.active_connections:
            self.active_connections[contest_id] = []
        self.active_connections[contest_id].append(websocket)

    def disconnect(self, websocket: WebSocket, contest_id: int):
        if contest_id in self.active_connections:
            self.active_connections[contest_id].remove(websocket)

    async def broadcast(self, message: dict, contest_id: int):
        if contest_id in self.active_connections:
            for connection in self.active_connections[contest_id]:
                await connection.send_json(message)

manager = ConnectionManager()