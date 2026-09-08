# FastAPI Pincode API

A FastAPI-based REST API for Indian pincode lookup. The project demonstrates API development with FastAPI, Pydantic validation, custom exception handling, and bulk pincode search functionality.

## Features

* Lookup location details using a pincode
* Custom validation for pincodes
* Custom exception handling
* Bulk pincode lookup endpoint
* Structured API responses using Pydantic models
* Interactive Swagger documentation

## Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

```text
FastApi/
├── main.py
├── models.py
├── exceptions.py
├── data.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/mohitghansela/fastapi-pincode-api.git
cd fastapi-pincode-api
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "Welcome to the Pincode Lookup API!"
}
```

### Lookup Pincode

```http
GET /pincode/{pincode}
```

Example:

```http
GET /pincode/110001
```

Response:

```json
{
  "pincode": "110001",
  "city": "New Delhi",
  "state": "Delhi",
  "country": "India"
}
```

### Bulk Lookup

```http
POST /bulk
```

Request:

```json
{
  "pincodes": [
    "110001",
    "400001",
    "560001"
  ]
}
```

Response:

```json
[
  {
    "pincode": "110001",
    "city": "New Delhi",
    "state": "Delhi",
    "country": "India"
  }
]
```

## Author

Mohit Ghansela
