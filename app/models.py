from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id: int = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(50), nullable=False)
    content: str = Column(String(1000), nullable=False)
    published: bool = Column(Boolean, server_default='1', nullable=False)
    created_at: TIMESTAMP = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id: int = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, nullable=False)
    email: str = Column(String(20), nullable=False, unique=True)
    password: str = Column(String(100), nullable=False)
    created_at: TIMESTAMP = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))  