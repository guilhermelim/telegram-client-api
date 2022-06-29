import uvicorn
from fastapi import FastAPI
from telegram_client_api.client import (connect, get_dialogs)


app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/dialogs")
async def dialogs():
    return await get_dialogs()


def start():
    connect()
    uvicorn.run("telegram_client_api.main:app", host="127.0.0.1", port=8000, reload=True, workers=2)
