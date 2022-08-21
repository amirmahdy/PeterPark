# PeterPark

This application is designed to write (validated) German licence plates, return and search over with Levenshtein distance variable.

This application is written in Flask and is using Postgresql as database.

## Deployment

To deploy this project run

```bash
  sudo docker-compose up --build -d
```

Note:
The application utilizes docker, it is necessary to have docker service up and running on the machine.

Note:
After successfully runnging the application you can navigate to :
http://127.0.0.1:5000/api/docs

## API Reference

#### Get all items

```http
  GET /plate
```

Returns all licence plates registerd.

#### Insert an item

```http
  POST /plate
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `plate`      | `string` | **Required**. Licence plate to register |

#### Seach for an Item

Validates the input licence plate, returns responses with 200, 400, 422 state.


```http
  GET /search-plate
```

| Query String | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `key`      | `string` | **Required**. Keyword to search |
| `levenshtein`      | `string` | **Required**. Levenshtein dist|

Return licence plates with appropriate dist from key.



## Running Tests

To run tests locally, navigate to project root dir.


Create a virtual env.
```bash
  python3 -m venv venv
```
Activate the virtual env.
```bash
  source venv/bin/activate
```
Install requirements
```bash
  pip install -r requirements.txt
```
Now you can test and also run application locally. 
```bash
  pytest src/plate/test 
```



