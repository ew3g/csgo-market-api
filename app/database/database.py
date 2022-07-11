from bson.objectid import ObjectId
from ..models.item import item_helper

import motor.motor_asyncio
import os


class Database:

    url = None
    client = None
    database = None
    item_collection = None

    def __init__(self):
        self.url = os.getenv("DATABASE_URL")
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.url)
        self.database = self.client['cs-info']
        self.item_collection = self.database.get_collection("item")

    async def retrieve_items(self, page, limit):
        items = []
        count = await self.item_collection.count_documents({})
        async for item in self.item_collection.find().skip(page * limit).limit(limit):
            items.append(item_helper(item))
        return items, count

    async def add_item(self, item_data: dict) -> dict:
        item = await self.item_collection.insert_one(item_data)
        new_item = await self.item_collection.find_one({"_id": item.inserted_id})
        return item_helper(new_item)

    async def retrieve_item(self, item_id: str) -> dict:
        item = await self.item_collection.find_one({"_id": ObjectId(item_id)})
        if item:
            return item_helper(item)

    async def update_item(self, item_id: str, data: dict):
        if len(data) < 1:
            return False
        item = await self.item_collection.find_one({"_id": ObjectId(item_id)})
        if item:
            updated_item = await self.item_collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})
            if updated_item:
                return True
            return False

    async def delete_item(self, item_id: str):
        item = await self.item_collection.find_one({"_id": ObjectId(item_id)})
        if item:
            await self.item_collection.delete_one({"_id": ObjectId(item_id)})
            return True
