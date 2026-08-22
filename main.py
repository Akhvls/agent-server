from fastapi import FastAPI, WebSocket

app = FastAPI()

message_table = []

@app.get("/")
def home():
    return {"status": "truee"}

@app.get("/other")
def main():
     return {"status": "true"}

@app.websocket("/ws")
async def echo(websocket: WebSocket):
    await websocket.accept()
    print("test to accept")
    while True:
        message = await websocket.receive_text()
        message_table.append(message)
        await websocket.send_text(f"message log: {message_table}")

