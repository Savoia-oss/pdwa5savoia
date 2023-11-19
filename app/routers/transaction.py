from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/transactions",
    tags=['Transactions']
)

@router.post("/")
def create_transaction(transaction: schemas.TransactionBase,db: Session = Depends(get_db)):
    new_transaction = models.Transaction(**transaction.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

@router.get("/{userId}")
def view_transaction():
    return{"data": "Transaction of the user"}