from sqlalchemy.orm import Session

import models, schemas


def get_books(db: Session):
    return db.query(models.BookModel).all()


def add_book(db: Session, book_name: str, author_name: str, path: str):
    db_book = models.BookModel(book_name=book_name, author_name=author_name, path=path)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
