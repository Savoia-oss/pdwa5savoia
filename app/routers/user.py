from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login_user():
    return{"data": "User logged"}

@router.put("/{id}", response_model=schemas.UserResponse)
def edit_user(id: int, user_updated: schemas.UserCreate, db: Session = Depends(get_db)):
    user_edited = db.query(models.Item).filter(models.User.id_user == id)

    user = user_edited.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id:{id} does not exists")
    
    user_edited.update(user_updated.dict(), synchronize_session=False)

    db.commit()

    return user_edited.first()

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user_deleted = db.query(models.User).filter(models.User.id_user == id)

    if user_deleted.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} does not exists")
    
    user_deleted.delete(synchronize_session=False)
    db.commit()
    
    return user_deleted