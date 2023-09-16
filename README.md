sk CRUD API

This is a simple Flask CRUD (Create, Read, Update, Delete) API that interacts with a MySQL database to manage a list of persons.

## Table of Contents

- [API Endpoints](#api-endpoints)
  - [Get All Persons](#get-all-persons)
  - [Get a Person by ID](#get-a-person-by-id)
  - [Create a Person](#create-a-person)
  - [Update a Person](#update-a-person)
  - [Delete a Person](#delete-a-person)
- [Usage](#usage)
  - [Example Usage](#example-usage)
- [License](#license)

## API Endpoints

### Get All Persons

- **URL**: `/api/all`
- **Method**: `GET`
- **Description**: Get all persons.
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: A JSON array of persons.

### Get a Person by ID

- **URL**: `/api/<int:person_id>`
- **Method**: `GET`
- **Description**: Get a person by ID.
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: JSON object representing the person.
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**: `{ "error": "Person not found" }`

### Create a Person

- **URL**: `/api`
- **Method**: `POST`
- **Description**: Create a new person.
- **Request Body**: JSON object with a "name" field representing the person's name.
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: JSON object representing the newly created person.
- **Error Response**:
  - **Code**: 400 Bad Request
  - **Content**: `{ "error": "Bad request" }`

### Update a Person

- **URL**: `/api/<int:person_id>`
- **Method**: `PUT`
- **Description**: Update a person.
- **Request Body**: JSON object with a "name" field representing the new name for the person.
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: JSON object representing the updated person.
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**: `{ "error": "Person not found" }`

### Delete a Person

- **URL**: `/api/<int:person_id>`
- **Method**: `DELETE`
- **Description**: Delete a person.
- **Success Response**:
  - **Code**: 200 OK
  - **Content**: `{ "Success": "Person deleted successfully" }`
- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**: `{ "error": "Person not found" }`

## Usage

You can use any API testing tool (e.g., Postman) to interact with the API endpoints mentioned above.

### Example Usage

- **Get All Persons**:

```bash
curl http://localhost:5000/api/all
