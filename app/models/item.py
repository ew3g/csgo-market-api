from pydantic import BaseModel, Field


class ItemSchema(BaseModel):
    name: str = Field()
    type: str = Field()
    subtype: str = Field()
    game_type: str = Field()

    class Config:
        schema_extra = {
            "example": {
                "name": "★ Bowie Knife | Case Hardened (Well-Worn)",
                "type": "weapon",
                "subtype": "knife",
                "game_type": "★ Covert Knife"
            }
        }


def get_response_model(data, message, code=200):
    return {
        "data": data,
        "code": code,
        "message": message
    }


def get_response_list_model(data, page, total_items, message, code=200):
    return {
        "data": data,
        "code": code,
        "message": message,
        "page": page,
        "total_elements": total_items
    }


def get_error_response_model(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }


def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "type": item["type"],
        "subtype": item["subtype"],
        "game_type": item["game_type"],
    }
