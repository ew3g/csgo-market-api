from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from starlette.requests import Request
import uvicorn
import dotenv


from app.internal import admin
from app.routers import item


dotenv.load_dotenv()

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(admin.router)
app.include_router(item.router)


@app.get("/ping")
@limiter.limit("1/second")
async def root(request: Request):
    return {"message": "OK"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
