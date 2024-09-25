from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class BookModel(Base):
    __tablename__ = "Book"

    id = Column(Integer, primary_key=True)
    book_name = Column(String, unique=True, index=True)
    author_name = Column(String, unique=True, index=True)
    path = Column(String, unique=True, index=True)
