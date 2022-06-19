from fastapi import FastAPI
import uvicorn
import dotenv

from app.internal import admin
from app.routers import item


dotenv.load_dotenv()

app = FastAPI()

app.include_router(admin.router)
app.include_router(item.router)


@app.get('/ping')
async def root():
    return {'message': 'OK'}

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", reload=True)
