from fastapi import APIRouter, Depends
from slowapi import Limiter
from slowapi.util import get_remote_address
from starlette.requests import Request

from ..dependencies import get_token_header

limiter = Limiter(key_func=get_remote_address)
router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)])


@router.post("/")
@limiter.limit("1/second")
async def update_admin(request: Request):
    return {"message": "Admin getting schwifty"}
