<!-- markdownlint-configure-file {
  "MD013": {
    "code_blocks": false,
    "tables": false
  },
  "MD033": false,
  "MD041": false
} -->

<div align="center">

# CSGO Market API

[![GitHub license](https://img.shields.io/github/license/ew3g/csgo-market-api.svg)](https://github.com/ew3g/csgo-market-api/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/ew3g/csgo-market-api.svg)](https://github.com/ew3g/csgo-market-api/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/ew3g/csgo-market-api.svg)](https://github.com/ew3g/csgo-market-api/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/ew3g/csgo-market-api.svg)](https://gitHub.com/ew3g/csgo-market-api/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/ew3g/csgo-market-api.svg?style=social&label=Watch)](https://github.com/ew3g/csgo-market-api/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/ew3g/csgo-market-api.svg?style=social&label=Fork)](https://gitHub.com/ew3g/csgo-market-api/network/)
[![GitHub stars](https://img.shields.io/github/stars/ew3g/csgo-market-api.svg?style=social&label=Star)](https://gitHub.com/ew3g/csgo-market-api/stargazers/)

![Counter Strike Logo](https://github.com/ew3g/csgo-market-api/blob/main/csgo-icon.png?raw=true "Sample inline image")

This project is a REST API to a Steam Market Item model. It was built with [FastApi](https://fastapi.tiangolo.com) and uses [MongoDB](https://www.mongodb.com/) as datasource.
<!-- https://github.com/bbc/REST-API-example/blob/master/README.md -->
[Installation](#installation) • [Usage](#usage)
</div>

It is recommended to run this API with the [CSGO Market Crawler](https://github.com/ew3g/csgo-market-crawler), as it is responsible for populating the base with Steam Market items
## Installation
- Set up a MongoDB database, I used a free tier [Atlas MongoDB](https://www.mongodb.com/atlas/database).
- Use package manager [pip](https://pip.pypa.io/en/stable/) to install all needed libs.
```bash pip install -r requirements.txt```

- Create the file .env in the project root folder with the following content:

```
DATABASE_URL='mongodb+srv://USER:PASSWORD@HOST/DATABASE?retryWrites=true&w=majority'
LOG_LEVEL='INFO'
```  

## Usage
To run this project is very simple, run the server with: 
```
$ uvicorn main:app --reload
```
or
```
$ python main.py
```

## REST API
Endpoints available are the following:

### Get list of all items

#### Request
`GET /item`

    curl --location --request GET 'http://localhost:8000/item/' \
    --header 'x-token: my_token'

#### Response
    HTTP/1.1 200 OK
    Date: Mon, 13 Jun 2022 18:02:48 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 261

    {
      "data":[
        "id": "96840fb2734935e846da",
        "name": "Item Name",
        "type": "Item Type",
        "subtype": "Item Subtype",
        "game_type": "Item Game Type"
      ],
      "code": 200,
      "message": "Items data retrieved succesfully"
    }

### Get a specific item by id

#### Request
`GET /item/{id}`

    curl --location --request GET 'localhost:8000/item/629d4b340fb273faf5e846da' \
    --header 'x-token: my_token'

#### Response
    HTTP/1.1 200 OK
    Date: Mon, 13 Jun 2022 18:02:48 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 289

    {
        "data": {
            "id": "96840fb2734935e846da",
            "name": "Item Name",
            "type": "Item Type",
            "subtype": "Item Subtype",
            "game_type": "Item Game Type"
        },
        "code": 200,
        "message": "Item data retrieved succesfully"
    }

### Create an item

#### Request
`POST /item`

    curl --location --request POST 'http://localhost:8000/item' \
    --header 'x-token: my_token' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "Item Name",
        "type": "Item Type",
        "subtype": "Item Subtype",
        "game_type": "Item Game Type"
    }'

#### Response
    HTTP/1.1 200 OK
    Date: Mon, 13 Jun 2022 18:02:48 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 182

    {
        "data": {
            "id": "62ab3c195fd7d6594c281d61",
            "name": "Item Name",
            "type": "Item Type",
            "subtype": "Item Subtype",
            "game_type": "Item Game Type"
        },
        "code": 201,
        "message": "Item addeed successfully"
    }

### Update an item

#### Request
`PUT /item/{id}`

    curl --location --request PUT 'http://localhost:8000/item/62ab40abcc85842901cf85ef' \
    --header 'x-token: my_token' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "Item Name",
        "type": "Item Type",
        "subtype": "Item Subtype",
        "game_type": "Item Game Type"
    }'

#### Response
    HTTP/1.1 200 OK
    Date: Mon, 13 Jun 2022 18:02:48 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 151

    {
        "data": {
            "name": "Item Name",
            "type": "Item Type",
            "subtype": "Item Subtype",
            "game_type": "Item Game Type"
        },
        "code": 200,
        "message": "Item updated successfully"
    }

### Delete an item

#### Request
`DELETE /item/{id}`

    curl --location --request DELETE 'http://localhost:8000/item/62ab40abcc85842901cf85ef?x-token=my_token' \
    --header 'x-token: my_token'

#### Response
    HTTP/1.1 200 OK
    Date: Mon, 13 Jun 2022 18:02:48 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 83

    {
        "data": "62ab40abcc85842901cf85ef",
        "code": 200,
        "message": "Item deleted succesfully"
    }


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[The MIT License (MIT)](https://mit-license.org/)

## Thanking
CSGO png image for the project icon [csgo-icon](https://www.freeiconspng.com/img/42849). Credits to Ahkâm.

API png image for the project icon [api-icon](https://www.flaticon.com/free-icon/cloud-computing_4230906). Credits to [Freepik](https://www.flaticon.com/authors/freepik).