from fastapi import Header, HTTPException
import os

API_TOKEN = os.getenv('API_TOKEN')


async def get_token_header(x_token: str = Header()):
    if x_token != API_TOKEN:
        raise HTTPException(status_code=400, detail='X-Token header invalid')
