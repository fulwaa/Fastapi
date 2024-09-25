from pydantic import BaseModel
from fastapi import UploadFile


class BookBase(BaseModel):
    book_name: str
    author_name: str


class BookCreate(BookBase):
    path: str


class Book(BookBase):
    book_id: int

    class Config:
        orm_mode = True


class BookFile(BaseModel):
    file: UploadFile
    book_name: str
    author_name: str
