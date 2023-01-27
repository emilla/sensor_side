# Importing the relevant libraries
import websockets
import asyncio

# Server data
address = "atom-radpi-01.local"
PORT = 7890
print("Server listening on Port " + str(PORT))

# A set of connected ws clients
connected = set()

# The main behavior function for this server
# This func is called echo because it just takes the message and sends it back with the "await conn.send(..)" line
async def echo(websocket, path):
    print("A client just connected")
    # Store a copy of the connected client
    connected.add(websocket)
    # Handle incoming messages
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            
            # Send a response to all connected clients
            for conn in connected:
                msg = input("Type a message:")
                await conn.send(msg)
          

    # Handle disconnecting clients 
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        connected.remove(websocket)

# Start the server
start_server = websockets.serve(echo, address, PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
