from dotenv import load_dotenv, find_dotenv
from fastapi import APIRouter, Body, Depends
from slowapi import Limiter
from slowapi.util import get_remote_address
from starlette.requests import Request
from fastapi.encoders import jsonable_encoder

from app.models.item import (
    get_response_model,
    get_response_list_model,
    get_error_response_model,
    ItemSchema,
)
from ..dependencies import get_token_header
from ..database.database import Database

load_dotenv(find_dotenv())

limiter = Limiter(key_func=get_remote_address)
db = Database()

router = APIRouter(
    prefix='/item',
    tags=['item'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not found'}}
)


@router.post('/', response_description='Item data added into the database')
@limiter.limit("1/second")
async def add_item_data(request: Request, item: ItemSchema = Body(...)):
    item = jsonable_encoder(item)
    new_item = await db.add_item(item)
    return get_response_model(new_item, 'Item addeed successfully', 201)


@router.get('/')
@limiter.limit("1/second")
async def get_items_data(request: Request, page: int = 0, limit: int = 10):
    items, total_items = await db.retrieve_items(page, limit)
    if items:
        return get_response_list_model(items, page, total_items, 'Items data retrieved succesfully')
    return get_response_model(items, 'Empty list returned')


@router.get('/{item_id}')
@limiter.limit("1/second")
async def get_item_data(request: Request, item_id: str):
    item = await db.retrieve_item(item_id)
    if item:
        return get_response_model(item, 'Item data retrieved succesfully')
    return get_error_response_model('An error ocurred.', 404, 'Item doesn\'t exist')


@router.put('/{item_id}')
@limiter.limit("1/second")
async def update_item_data(request: Request, item_id: str, item: dict):
    status_update = await db.update_item(item_id, item)
    if status_update:
        return get_response_model(item, 'Item updated successfully')
    return get_error_response_model('An error ocurred.', 500, 'Failed to update item')


@router.delete('/{item_id}')
@limiter.limit("1/second")
async def delete_item_data(request: Request, item_id: str):
    status_delete = await db.delete_item(item_id)
    if status_delete:
        return get_response_model(item_id, 'Item deleted succesfully')
    return get_error_response_model('An error occurred.', 500, 'Failed to delete item')
