# Implementation Guide

## Overview

This document provides detailed instructions for implementing the project, including code snippets and examples for key components, database schema and migrations, and information on testing and debugging.

## Project Structure

The project follows a modular structure to ensure maintainability and scalability. Below is an overview of the project structure:

```
project-root/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── content.py
│   └── tests/
│       ├── __init__.py
│       ├── test_users.py
│       └── test_content.py
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── alembic.ini
├── requirements.txt
└── README.md
```

## Key Components

### 1. FastAPI Application

The main FastAPI application is defined in `app/main.py`. This file initializes the FastAPI app, includes the routers, and sets up the middleware.

```python
from fastapi import FastAPI
from app.routers import users, content

app = FastAPI()

app.include_router(users.router)
app.include_router(content.router)
```

### 2. Models

The database models are defined using SQLAlchemy in `app/models.py`. These models represent the database tables and their relationships.

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    contents = relationship("Content", back_populates="author")

class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="contents")
```

### 3. Schemas

The Pydantic schemas are defined in `app/schemas.py`. These schemas are used for data validation and serialization.

```python
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode: True

class ContentBase(BaseModel):
    title: str
    body: str

class ContentCreate(ContentBase):
    author_id: int

class Content(ContentBase):
    id: int

    class Config:
        orm_mode: True
```

### 4. CRUD Operations

The CRUD operations are defined in `app/crud.py`. These functions interact with the database to perform the necessary operations.

```python
from sqlalchemy.orm import Session
from app import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_content(db: Session, content_id: int):
    return db.query(models.Content).filter(models.Content.id == content_id).first()

def create_content(db: Session, content: schemas.ContentCreate):
    db_content = models.Content(title=content.title, body=content.body, author_id=content.author_id)
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content
```

### 5. Routers

The routers are defined in the `app/routers` directory. Each router corresponds to a specific set of endpoints.

#### Users Router (`app/routers/users.py`)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.dependencies import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
```

#### Content Router (`app/routers/content.py`)

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.dependencies import get_db

router = APIRouter()

@router.post("/content/", response_model=schemas.Content)
def create_content(content: schemas.ContentCreate, db: Session = Depends(get_db)):
    return crud.create_content(db=db, content=content)

@router.get("/content/{content_id}", response_model=schemas.Content)
def read_content(content_id: int, db: Session = Depends(get_db)):
    db_content = crud.get_content(db, content_id=content_id)
    if db_content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_content
```

## Database Schema and Migrations

The database schema is defined using SQLAlchemy models. Alembic is used for database migrations. The migration scripts are located in the `alembic/versions` directory.

### Example Migration Script

```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1234567890ab'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('hashed_password', sa.String),
    )
    op.create_table(
        'contents',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('body', sa.String),
        sa.Column('author_id', sa.Integer, sa.ForeignKey('users.id')),
    )

def downgrade():
    op.drop_table('contents')
    op.drop_table('users')
```

## Testing and Debugging

### Unit Tests

Unit tests are located in the `app/tests` directory. These tests use FastAPI's built-in testing client to simulate requests and validate the responses.

#### Example Unit Test (`app/tests/test_users.py`)

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "john_doe", "email": "john@example.com", "password": "password123"})
    assert response.status_code == 201
    assert response.json()["username"] == "john_doe"
    assert response.json()["email"] == "john@example.com"

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "john_doe"
    assert response.json()["email"] == "john@example.com"
```

### Debugging

To debug the application, you can use the following tools and techniques:

1. **Logging**: Use Python's built-in logging module to log important information and errors.
2. **Debugging Tools**: Use debugging tools such as `pdb` (Python Debugger) to set breakpoints and inspect the code.
3. **Interactive API Documentation**: FastAPI provides interactive API documentation using Swagger UI and ReDoc. Use these tools to explore and test the API endpoints.

## Conclusion

This implementation guide provides detailed instructions for setting up and implementing the project. By following the provided code snippets and examples, you can build a robust and scalable web application using FastAPI, Pydantic, and SQLAlchemy.
