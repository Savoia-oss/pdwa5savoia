from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/items",
    tags=['Items']
)

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    new_item = models.Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/", response_model=List[schemas.ItemResponse])
def get_item(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()

    if items == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"there is no items in the database")

    return items

@router.get("/{id}", response_model=schemas.ItemResponse)
def get_item_id(id: int, db: Session = Depends(get_db)):
    specific_item = db.query(models.Item).filter(models.Item.id_item == id).first()

    if specific_item == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id:{id} does not exists")

    return specific_item

@router.put("/{id}", response_model=schemas.ItemResponse)
def edit_item(id: int, item_updated: schemas.ItemCreate, db: Session = Depends(get_db)):
    item_edited = db.query(models.Item).filter(models.Item.id_item == id)

    item = item_edited.first()

    if item == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id:{id} does not exists")
    
    item_edited.update(item_updated.dict(), synchronize_session=False)

    db.commit()

    return item_edited.first()

@router.delete("/{id}", response_model=schemas.ItemResponse)
def delete_item(id: int, db: Session = Depends(get_db)):
    item_deleted = db.query(models.Item).filter(models.Item.id_item == id)

    if item_deleted.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id {id} does not exists")
    
    item_deleted.delete(synchronize_session=False)
    db.commit()

    return item_deleted

@router.get("/search")
def search_item():
    return{"data": "Searched"}

#def find_post(id):
#    for p in my_posts:
#        if p['id'] == id:
#            return p