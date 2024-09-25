from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
from fastapi import FastAPI, File, UploadFile, Form
import os
import aiofiles
from typing import Annotated


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# os.makedirs("files", exist_ok=True)


@app.get("/get_books")
async def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db=db)


@app.post("/add_book")
async def addi_book(
    book_file: Annotated[UploadFile, File()],
    book_name: Annotated[str, Form()],
    author_name: Annotated[str, Form()],
    db: Session = Depends(get_db),
):
    file_path = f"files/{book_file.filename}"
    async with aiofiles.open(file_path, "wb") as out_file:
        content = book_file.file.read()
        out_file.write(content)
    db_book = crud.add_book(
        db, book_name=book_name, author_name=author_name, path=file_path
    )
    return db_book
