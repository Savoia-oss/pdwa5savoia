from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/categories",
    tags=['Categories']
)

@router.get("/")
def get_categories():
    return{"data": "Here are all your categories"}

@router.post("/categories")
def create_category():
    return{"data": "Category created"}

@router.put("/categories/{id}")
def edit_category():
    return{"data": "Category edited"}

@router.delete("/categories/{id}")
def delete_category():
    return{"data": "Category deleted"}

