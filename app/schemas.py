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
