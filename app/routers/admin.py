from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/admin",
    tags=['Admins']
)

@router.post("/login")
def login_admin():
    return{"data": "Admin logged"}

@router.get("/reports", response_model=List[schemas.ItemResponse])
def get_reports(db: Session = Depends(get_db)):
    reports = db.query(models.Item).all()
    return reports

@router.get("/users", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users