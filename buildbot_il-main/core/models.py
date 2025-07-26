from uuid import uuid4
from sqlalchemy import Column, String, UUID, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from core.databases import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    phone = Column(String(20), unique=True)
    balance_bc = Column(Integer, default=0)  # 1 BC = 1 ₪
    is_banned = Column(Boolean, default=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    customer_id = Column(UUID, ForeignKey("users.id"))
    executor_id = Column(UUID, ForeignKey("users.id"), nullable=True)
    amount = Column(Integer)  # Сумма в BC
    status = Column(String(20), default="draft")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
