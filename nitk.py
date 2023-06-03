import asyncio
import websockets
import time
import sys

cName = sys.argv[1] if len(sys.argv)>=2 else "lol"
time1 = time.time()
data = list()
n = 0


async def send_messages(websocket):
    global n, time1, data
    while True:
        if(len(data) >= 5):
            await websocket.send(f"Client {cName} received {n} blocks in {time.time() - time1} time")
            data.clear()
            n=0
            time1 = time.time()
        await asyncio.sleep(0)

# async def send_messages(websocket):
#     while True:
#         await websocket.send("Hey Server!")
#         await asyncio.sleep(1)


async def receive_messages(websocket):
    global n, data
    while True:
        message = await websocket.recv()
        data.append(message)
        n += 1
        print(f"{int(time.time())} >>>Received message: {message}")


async def client():
    while True:
        try:
            async with websockets.connect("ws://localhost:8000") as websocket:
                # Create tasks to send and receive messages concurrently
                send_task = asyncio.create_task(send_messages(websocket))
                receive_task = asyncio.create_task(receive_messages(websocket))
                await asyncio.gather(send_task, receive_task)
        except:
            print("Trying to reconnect to server...")
            await asyncio.sleep(1)

asyncio.run(client())