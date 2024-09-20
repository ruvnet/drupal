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

@router.put("/content/{content_id}", response_model=schemas.Content)
def update_content(content_id: int, content: schemas.ContentUpdate, db: Session = Depends(get_db)):
    db_content = crud.get_content(db, content_id=content_id)
    if db_content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return crud.update_content(db=db, content_id=content_id, content=content)

@router.delete("/content/{content_id}")
def delete_content(content_id: int, db: Session = Depends(get_db)):
    db_content = crud.get_content(db, content_id=content_id)
    if db_content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    crud.delete_content(db=db, content_id=content_id)
    return {"message": "Content deleted successfully"}
