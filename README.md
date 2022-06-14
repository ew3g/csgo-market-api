<!-- markdownlint-configure-file {
  "MD013": {
    "code_blocks": false,
    "tables": false
  },
  "MD033": false,
  "MD041": false
} -->

<div align="center">

# CSGO Market Crawler

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

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## REST API
Endpoints available are the following:

### Get list of all items

#### Request
`GET /items`

    curl -i -H 'Accept: application/json' http://localhost:8000/items

#### Response
    HTTP/1.1 200 OK
    Date: Mon, 13 Jun 2022 18:02:48 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[The MIT License (MIT)](https://mit-license.org/)

## Thanking
CSGO png image for the project icon [csgo-icon](https://www.freeiconspng.com/img/42849). Credits to Ahkâm.

Crawler png image for the project icon [crawler-icon](https://www.flaticon.com/free-icon/web_1792126). Credits to [Pixelmeetup](https://www.flaticon.com/authors/pixelmeetup).