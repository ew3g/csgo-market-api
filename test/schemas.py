unprocessable_entity_response_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "detail": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "loc": {
              "type": "array",
              "items": [
                {
                  "type": "string"
                },
                {
                  "type": "string"
                }
              ]
            },
            "msg": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          },
          "required": [
            "loc",
            "msg",
            "type"
          ]
        }
      ]
    }
  },
  "required": [
    "detail"
  ]
}

item_list_response_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "subtype": {
              "type": "string"
            },
            "game_type": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "type",
            "subtype",
            "game_type"
          ]
        }
      ]
    },
    "code": {
      "type": "integer"
    },
    "message": {
      "type": "string"
    },
    "page": {
      "type": "integer"
    },
    "total_elements": {
      "type": "integer"
    }
  },
  "required": [
    "data",
    "code",
    "message",
    "page",
    "total_elements"
  ]
}

empty_item_list_response_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {}
    },
    "code": {
      "type": "integer"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "data",
    "code",
    "message"
  ]
}

item_response_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "type": {
          "type": "string"
        },
        "subtype": {
          "type": "string"
        },
        "game_type": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name",
        "type",
        "subtype",
        "game_type"
      ]
    },
    "code": {
      "type": "integer"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "data",
    "code",
    "message"
  ]
}

item_not_found_response_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    },
    "code": {
      "type": "integer"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "error",
    "code",
    "message"
  ]
}