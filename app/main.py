from datetime import date
from typing import List
from fastapi import FastAPI, Depends
from fastapi.params import Body
from pydantic import BaseModel, Field, ValidationError
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
from .routers import item, user, transaction, admin, category

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(item.router)
app.include_router(transaction.router)
app.include_router(admin.router)
app.include_router(category.router)

