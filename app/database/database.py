import dotenv
import motor.motor_asyncio
import os
from bson.objectid import ObjectId
dotenv.load_dotenv()
print('jdsdjaskldjsaldsakdljaskldjaskldjas')
url = os.getenv('DATABASE_URL')
client = motor.motor_asyncio.AsyncIOMotorClient(url)

database = client['cs-info']
item_collection = database.get_collection('item')

#helpers

def item_helper(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'type': item['type'],
        'subtype': item['subtype'],
        'game_type': item['game_type'],
    }
    
async def retrieve_items():
    print(url)
    items = []
    async for item in item_collection.find():
        items.append(item_helper(item))
    return items

async def add_item(item_data: dict) -> dict:
    item = await item_collection.insert_one(item_data)
    new_item = await item_collection.find_one({'_id': item['inserted_id']})
    return item_helper(new_item)

async def retrieve_item(id: str) -> dict:
    print('okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    print(url)
    print(id)
    item = await item_collection.find_one({'_id': ObjectId(id)})
    if item:
        return item_helper(item)
    
async def update_item(id: str, data: dict):
    if len(data) < 1:
        return False
    item = await item_collection.find_one({'_id': ObjectId(id)})
    if item:
        updated_item = await item_collection.update_one({'_id': ObjectId(id), '$set': data})
        if updated_item:
            return True
        return False
    
async def delete_item(id: str):
    item = await item_collection.find_one({'_id': ObjectId(id)})
    if item:
        await item_collection.delete_one({'_id': ObjectId(id)})
        return True