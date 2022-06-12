from fastapi import APIRouter, Body, Depends, HTTPException
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

fake_items_db = {'plumbus': {'name': 'Plumbus'}, 'gun': {'name': 'Portal Gun'}}

@router.post('/', response_description='Item data added into the database')
async def add_item_data(item: ItemSchema = Body(...)):
    item = jsonable_encoder(item)
    new_item = await add_item(item)
    return ResponseModel(new_item, 'Item addeed successfully')

@router.get('/')
async def get_items():
    items = await retrieve_items()
    if items:
        return ResponseModel(items, 'Items data retrieved succesfully')
    return ResponseModel(items, 'Empty list returned')

@router.get('/{item_id}')
async def get_item(item_id: str):
    item = await retrieve_item(item_id)
    if item:
        return ResponseModel(item, 'Item data retrieved succesfully')
    return ErrorResponseModel('An error ocurred.', 404, 'Item doesn\'t exist' )

@router.put('/{item_id}', responses={403: {'description': 'Forbidden'}})
async def update_item(item_id: str):
    if item_id != 'plumbus':
        raise HTTPException(status_code=403, detail='You can only update the item: plumbus')
    return {'item_id': item_id, 'name': 'The great Plumbus'}