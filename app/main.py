from fastapi import Depends, FastAPI
import dotenv
import os
import uvicorn

#uvicorn app.main:app --reload
from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items


app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(items.router)
app.include_router(admin.router,
                   prefix='/admin',
                   tags=['admin'],
                   dependencies=[Depends(get_token_header)],
                   responses={418: {'description': 'I am a teapot'}})

@app.get('/')
async def root():
    """Application Root Method, to be implemented

    Returns:
        _type_: str
    """
    return {'message': 'Hello Bigger Aplications'}

# if __name__ == '__main__':
#     uvicorn.run('app.main:app', host="0.0.0.0", reload=True)