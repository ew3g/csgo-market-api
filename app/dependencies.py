from fastapi import Header, HTTPException
import os


async def get_token_header(x_token: str = Header()):
    if x_token != os.getenv("API_TOKEN"):
        raise HTTPException(status_code=400, detail="X-Token header invalid")
