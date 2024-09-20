from sqlalchemy.orm import Session
from app import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db_user.hashed_password = user.password
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_content(db: Session, content_id: int):
    return db.query(models.Content).filter(models.Content.id == content_id).first()

def create_content(db: Session, content: schemas.ContentCreate):
    db_content = models.Content(title=content.title, body=content.body, author_id=content.author_id)
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

def update_content(db: Session, content_id: int, content: schemas.ContentUpdate):
    db_content = db.query(models.Content).filter(models.Content.id == content_id).first()
    if db_content:
        db_content.title = content.title
        db_content.body = content.body
        db.commit()
        db.refresh(db_content)
    return db_content

def delete_content(db: Session, content_id: int):
    db_content = db.query(models.Content).filter(models.Content.id == content_id).first()
    if db_content:
        db.delete(db_content)
        db.commit()
    return db_content
