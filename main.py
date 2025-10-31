from fastapi import FastAPI, Depends, HTTPException
import Service, model, schema
from db import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/books/", response_model=list[schema.Book])
def get_all_books(db: Session = Depends(get_db)):
    return Service.get_books()

@app.post("/books/", response_model=schema.Book)
def create_new_book(book: schema.BookCreate, db: Session = Depends(get_db)):
    return Service.create_book(db, book)