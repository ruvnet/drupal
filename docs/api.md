# API Documentation

## Overview

This document provides detailed information about the API endpoints, their usage, request and response examples, authentication and authorization mechanisms, and error handling and status codes for implementing Drupal in Python using FastAPI, Pydantic, and SQLAlchemy.

## API Endpoints

### 1. User Endpoints

#### 1.1. Create User

- **Endpoint**: `/api/users`
- **Method**: `POST`
- **Description**: Create a new user.
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "username": "string",
    "email": "string"
  }
  ```

#### 1.2. Get User

- **Endpoint**: `/api/users/{user_id}`
- **Method**: `GET`
- **Description**: Retrieve user details by user ID.
- **Response**:
  ```json
  {
    "id": "integer",
    "username": "string",
    "email": "string"
  }
  ```

#### 1.3. Update User

- **Endpoint**: `/api/users/{user_id}`
- **Method**: `PUT`
- **Description**: Update user details by user ID.
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "username": "string",
    "email": "string"
  }
  ```

#### 1.4. Delete User

- **Endpoint**: `/api/users/{user_id}`
- **Method**: `DELETE`
- **Description**: Delete user by user ID.
- **Response**:
  ```json
  {
    "message": "User deleted successfully"
  }
  ```

### 2. Content Endpoints

#### 2.1. Create Content

- **Endpoint**: `/api/content`
- **Method**: `POST`
- **Description**: Create new content.
- **Request Body**:
  ```json
  {
    "title": "string",
    "body": "string",
    "author_id": "integer"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "title": "string",
    "body": "string",
    "author_id": "integer"
  }
  ```

#### 2.2. Get Content

- **Endpoint**: `/api/content/{content_id}`
- **Method**: `GET`
- **Description**: Retrieve content details by content ID.
- **Response**:
  ```json
  {
    "id": "integer",
    "title": "string",
    "body": "string",
    "author_id": "integer"
  }
  ```

#### 2.3. Update Content

- **Endpoint**: `/api/content/{content_id}`
- **Method**: `PUT`
- **Description**: Update content details by content ID.
- **Request Body**:
  ```json
  {
    "title": "string",
    "body": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "title": "string",
    "body": "string",
    "author_id": "integer"
  }
  ```

#### 2.4. Delete Content

- **Endpoint**: `/api/content/{content_id}`
- **Method**: `DELETE`
- **Description**: Delete content by content ID.
- **Response**:
  ```json
  {
    "message": "Content deleted successfully"
  }
  ```

### 3. Taxonomy Endpoints

#### 3.1. Create Taxonomy Term

- **Endpoint**: `/api/taxonomy`
- **Method**: `POST`
- **Description**: Create a new taxonomy term.
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "description": "string"
  }
  ```

#### 3.2. Get Taxonomy Term

- **Endpoint**: `/api/taxonomy/{term_id}`
- **Method**: `GET`
- **Description**: Retrieve taxonomy term details by term ID.
- **Response**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "description": "string"
  }
  ```

#### 3.3. Update Taxonomy Term

- **Endpoint**: `/api/taxonomy/{term_id}`
- **Method**: `PUT`
- **Description**: Update taxonomy term details by term ID.
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "description": "string"
  }
  ```

#### 3.4. Delete Taxonomy Term

- **Endpoint**: `/api/taxonomy/{term_id}`
- **Method**: `DELETE`
- **Description**: Delete taxonomy term by term ID.
- **Response**:
  ```json
  {
    "message": "Taxonomy term deleted successfully"
  }
  ```

## Authentication and Authorization

### Authentication

The API uses token-based authentication. Users must include a valid token in the `Authorization` header of their requests.

- **Header**:
  ```
  Authorization: Bearer <token>
  ```

### Authorization

The API uses role-based access control (RBAC) to manage permissions. Each user is assigned one or more roles, and each role has specific permissions.

## Error Handling and Status Codes

The API uses standard HTTP status codes to indicate the success or failure of a request. The following are common status codes used in the API:

- **200 OK**: The request was successful.
- **201 Created**: The resource was successfully created.
- **400 Bad Request**: The request was invalid or cannot be processed.
- **401 Unauthorized**: Authentication is required and has failed or has not yet been provided.
- **403 Forbidden**: The user does not have the necessary permissions for the resource.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: An error occurred on the server.

## Examples

### Example 1: Create User

**Request**:
```http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Response**:
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com"
}
```

### Example 2: Get Content

**Request**:
```http
GET /api/content/1 HTTP/1.1
Host: example.com
Authorization: Bearer <token>
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "title": "Sample Content",
  "body": "This is a sample content.",
  "author_id": 1
}
```

### Example 3: Update User

**Request**:
```http
PUT /api/users/1 HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "username": "john_doe_updated",
  "email": "john_updated@example.com",
  "password": "newpassword123"
}
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "username": "john_doe_updated",
  "email": "john_updated@example.com"
}
```

### Example 4: Delete Content

**Request**:
```http
DELETE /api/content/1 HTTP/1.1
Host: example.com
Authorization: Bearer <token>
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Content deleted successfully"
}
```

### Example 5: Create Taxonomy Term

**Request**:
```http
POST /api/taxonomy HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "name": "Category",
  "description": "A sample category"
}
```

**Response**:
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "Category",
  "description": "A sample category"
}
```

### Example 6: Get Taxonomy Term

**Request**:
```http
GET /api/taxonomy/1 HTTP/1.1
Host: example.com
Authorization: Bearer <token>
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Category",
  "description": "A sample category"
}
```

### Example 7: Update Taxonomy Term

**Request**:
```http
PUT /api/taxonomy/1 HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "name": "Updated Category",
  "description": "An updated sample category"
}
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Updated Category",
  "description": "An updated sample category"
}
```

### Example 8: Delete Taxonomy Term

**Request**:
```http
DELETE /api/taxonomy/1 HTTP/1.1
Host: example.com
Authorization: Bearer <token>
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Taxonomy term deleted successfully"
}
```

### 4. Drupal Data Endpoints

#### 4.1. Create Drupal Data

- **Endpoint**: `/api/drupal-data`
- **Method**: `POST`
- **Description**: Create new Drupal data.
- **Request Body**:
  ```json
  {
    "data_type": "string",
    "data_value": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "data_type": "string",
    "data_value": "string"
  }
  ```

#### 4.2. Get Drupal Data

- **Endpoint**: `/api/drupal-data/{data_id}`
- **Method**: `GET`
- **Description**: Retrieve Drupal data details by data ID.
- **Response**:
  ```json
  {
    "id": "integer",
    "data_type": "string",
    "data_value": "string"
  }
  ```

#### 4.3. Update Drupal Data

- **Endpoint**: `/api/drupal-data/{data_id}`
- **Method**: `PUT`
- **Description**: Update Drupal data details by data ID.
- **Request Body**:
  ```json
  {
    "data_type": "string",
    "data_value": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "data_type": "string",
    "data_value": "string"
  }
  ```

#### 4.4. Delete Drupal Data

- **Endpoint**: `/api/drupal-data/{data_id}`
- **Method**: `DELETE`
- **Description**: Delete Drupal data by data ID.
- **Response**:
  ```json
  {
    "message": "Drupal data deleted successfully"
  }
  ```

### 5. Taxonomy Endpoints

#### 5.1. Create Taxonomy Term

- **Endpoint**: `/api/taxonomy`
- **Method**: `POST`
- **Description**: Create a new taxonomy term.
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "description": "string"
  }
  ```

#### 5.2. Get Taxonomy Term

- **Endpoint**: `/api/taxonomy/{term_id}`
- **Method**: `GET`
- **Description**: Retrieve taxonomy term details by term ID.
- **Response**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "description": "string"
  }
  ```

#### 5.3. Update Taxonomy Term

- **Endpoint**: `/api/taxonomy/{term_id}`
- **Method**: `PUT`
- **Description**: Update taxonomy term details by term ID.
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "name": "string",
    "description": "string"
  }
  ```

#### 5.4. Delete Taxonomy Term

- **Endpoint**: `/api/taxonomy/{term_id}`
- **Method**: `DELETE`
- **Description**: Delete taxonomy term by term ID.
- **Response**:
  ```json
  {
    "message": "Taxonomy term deleted successfully"
  }
  ```

## Authentication and Authorization

### Authentication

The API uses token-based authentication. Users must include a valid token in the `Authorization` header of their requests.

- **Header**:
  ```
  Authorization: Bearer <token>
  ```

### Authorization

The API uses role-based access control (RBAC) to manage permissions. Each user is assigned one or more roles, and each role has specific permissions.

## Error Handling and Status Codes

The API uses standard HTTP status codes to indicate the success or failure of a request. The following are common status codes used in the API:

- **200 OK**: The request was successful.
- **201 Created**: The resource was successfully created.
- **400 Bad Request**: The request was invalid or cannot be processed.
- **401 Unauthorized**: Authentication is required and has failed or has not yet been provided.
- **403 Forbidden**: The user does not have the necessary permissions for the resource.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: An error occurred on the server.

## Examples

### Example 1: Create User

**Request**:
```http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123"
}
```

**Response**:
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com"
}
```

### Example 2: Get Content

**Request**:
```http
GET /api/content/1 HTTP/1.1
Host: example.com
Authorization: Bearer <token>
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "title": "Sample Content",
  "body": "This is a sample content.",
  "author_id": 1
}
```

### Example 3: Update User

**Request**:
```http
PUT /api/users/1 HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "username": "john_doe_updated",
  "email": "john_updated@example.com",
  "password": "newpassword123"
}
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "username": "john_doe_updated",
  "email": "john_updated@example.com"
}
```

### Example 4: Delete Content

**Request**:
```http
DELETE /api/content/1 HTTP/1.1
Host: example.com
Authorization: Bearer <token>
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Content deleted successfully"
}
```

### Example 5: Create Taxonomy Term

**Request**:
```http
POST /api/taxonomy HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "name": "Category",
  "description": "A sample category"
}
```

**Response**:
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "Category",
  "description": "A sample category"
}
```

### Example 6: Get Taxonomy Term

**Request**:
```http
GET /api/taxonomy/1 HTTP/1.1
Host: example.com
Authorization: Bearer <token>
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Category",
  "description": "A sample category"
}
```

### Example 7: Update Taxonomy Term

**Request**:
```http
PUT /api/taxonomy/1 HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer <token>

{
  "name": "Updated Category",
  "description": "An updated sample category"
}
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Updated Category",
  "description": "An updated sample category"
}
```

### Example 8: Delete Taxonomy Term

**Request**:
```http
DELETE /api/taxonomy/1 HTTP/1.1
Host: example.com
Authorization: Bearer <token>
```

**Response**:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Taxonomy term deleted successfully"
}
```
