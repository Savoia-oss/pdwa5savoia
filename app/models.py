from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text, null
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    status = Column(Boolean, server_default='TRUE', nullable=False)
    type = Column(String, nullable=False)
    start_date = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Item(Base):
    __tablename__ = "items"
    id_item = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Boolean, server_default='TRUE', nullable=False)
    edition_date = Column(Integer, nullable=False)
    frequency = Column(String, nullable=False)
    start_date = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id_user", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class Transaction(Base):
    __tablename__ = "transactions"
    id_transaction = Column(Integer, primary_key=True, nullable=False)
    price = Column(Float, nullable=False)
    start_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
"users.id_user", ondelete="CASCADE"), nullable=False)
    id_item = Column(Integer, ForeignKey(
        "items.id_item", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


