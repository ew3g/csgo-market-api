from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

from app.models.item import ErrorResponseModel, ItemSchema, ResponseModel
from ..dependencies import get_token_header
from ..database.database import(
    add_item,
    delete_item,
    retrieve_item,
    retrieve_items,
    update_item
)

router = APIRouter(
    prefix='/items',
    tags=['items'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not found'}}
)

@router.post('/', response_description='Item data added into the database')
async def add_item_data(item: ItemSchema = Body(...)):
    item = jsonable_encoder(item)
    new_item = await add_item(item)
    return ResponseModel(new_item, 'Item addeed successfully')

@router.get('/')
async def get_items_data():
    items = await retrieve_items()
    if items:
        return ResponseModel(items, 'Items data retrieved succesfully')
    return ResponseModel(items, 'Empty list returned')

@router.get('/{item_id}')
async def get_item_data(item_id: str):
    item = await retrieve_item(item_id)
    if item:
        return ResponseModel(item, 'Item data retrieved succesfully')
    return ErrorResponseModel('An error ocurred.', 404, 'Item doesn\'t exist' )

@router.put('/{item_id}')
async def update_item_data(item: dict):
    status_update = update_item(item['id'], item)
    if status_update:
        return ResponseModel(item, 'Item updated successfully')
    return ErrorResponseModel('An error ocurred.', 500, 'Failed to update item')

@router.delete('/{item_id}')
async def delete_item_data(item_id: str):
    status_delete = delete_item(item_id)
    if status_delete:
        return ResponseModel(item_id, 'Item deleted succesfully')
    return ErrorResponseModel('An error occurred.', 500, 'Failed to delete item')
