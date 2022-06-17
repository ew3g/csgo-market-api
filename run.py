from fastapi import FastAPI
import uvicorn

from app.internal import admin
from app.routers import item


app = FastAPI()

app.include_router(admin.router)
app.include_router(item.router)


@app.get('/ping')
async def root():
    return {'message': 'OK'}

if __name__ == '__main__':
    # uvicorn app.main:app --reload
    uvicorn.run('run:app', host="0.0.0.0", reload=True)
