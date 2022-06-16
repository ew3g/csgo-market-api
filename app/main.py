from fastapi import Depends, FastAPI
import uvicorn

from .dependencies import get_token_header
from .internal import admin
from .routers import items

app = FastAPI()

app.include_router(items.router)
app.include_router(admin.router,
                   prefix='/admin',
                   tags=['admin'],
                   dependencies=[Depends(get_token_header)],
                   responses={418: {'description': 'I am a teapot'}})


@app.get('/')
async def root():
    return {'message': 'Hello Bigger Aplications'}

if __name__ == '__main__':
    # uvicorn app.main:app --reload
    # uvicorn.run('app.main:app', host="0.0.0.0", reload=True)
    uvicorn.run('main:app', host="0.0.0.0", reload=True)