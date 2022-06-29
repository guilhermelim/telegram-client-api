# FastAPI imports
from multiprocessing.connection import wait
import uvicorn
from fastapi import FastAPI

# Telethon imports
from decouple import config
from telethon import TelegramClient

# Read environment variables from .env file
api_id = config('API_ID')
api_hash = config('API_HASH')

# Get username and return in JSON
async def getUsername():
    client = TelegramClient('anon', api_id, api_hash)
    await client.start()
    me = await client.get_me()
    await client.disconnect()
    return { "username": me.username }

async def getUsername_2():
    client = TelegramClient('anon', api_id, api_hash)
    await client.connect()
    if not client.is_user_authorized():
        return 'Login fail, need to run init_session'
    else:
        me = await client.get_me()
        await client.disconnect()
        return { "username": me.username }


# Define FastAPI object
app = FastAPI()

# Define API route
@app.get("/")
async def root():
    # return await getUsername()
    return await get_dialogs()

# Run the API server
def start():
    uvicorn.run("telegram_client_api.main:app", host="127.0.0.1", port=8000, reload=True, workers=2)
