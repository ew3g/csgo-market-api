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


def get_response_model(data, message):
    return {
        "data": [data],
        "code": 201,
        "message": message
    }


def get_error_response_model(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
