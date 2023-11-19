from pydantic import BaseModel, EmailStr
from datetime import datetime

class ItemBase(BaseModel):
    title: str
    category: str
    author: str
    price: float
    description: str
    status: bool
    edition_date: int
    frequency: str
    owner_id: int

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id_item: int
    start_date: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    type: str

class UserResponse(BaseModel):
    id_user: int
    email: EmailStr
    start_date: datetime

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    price: float
    owner_id: int
    id_item: int