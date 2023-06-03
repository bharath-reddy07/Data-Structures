import asyncio
import websockets
from faker import Faker
import time

fake = Faker()
test = "1"
clients = set()


async def send_messages(websocket):
    while True:
        await websocket.send(getMessage())
        # print(f">>>sent")
        await asyncio.sleep(1)

def getMessage():
    return fake.name()

async def receive_messages(websocket):
    while True:
        message = await websocket.recv()
        print(f"{int(time.time())} >>> Received message: {message}")


async def server(websocket, path):
    global clients
    try:
        clients.add(websocket)
        send_task = asyncio.create_task(send_messages(websocket))
        receive_task = asyncio.create_task(receive_messages(websocket))
        await asyncio.gather(send_task, receive_task)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
        clients.remove(websocket)


async def main():
    # Start the server
    async with websockets.serve(server, "localhost", 8000):
        await asyncio.Future()

asyncio.run(main())