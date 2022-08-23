from ast import Str
from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'title one', 'author': 'Author one'},
    'book_2': {'title': 'title two', 'author': 'Author two'},
    'book_3': {'title': 'title three', 'author': 'Author three'},
    'book_4': {'title': 'title four', 'author': 'Author four'},
    'book_5': {'title': 'title five', 'author': 'Author five'}
}


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get('/books/mybook')
async def read_favorite_book():
    return {'book_title': 'My favorite book '}


@app.get('/books/{book_id}')
async def read_book(book_id: int):
    return {'book_id': book_id}


@app.get('directions/{direction_name}')
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {'Direction': direction_name, 'sub': 'up'}
    if direction_name == DirectionName.south:
        return {'Direction': direction_name, 'sub': 'down'}
    if direction_name == DirectionName.east:
        return {'Direction': direction_name, 'sub': 'left'}
    if direction_name == DirectionName.west:
        return {'Direction': direction_name, 'sub': 'right'}


@app.get('/')
async def read_all_book(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0
    if len(BOOKS) > 0:
        for books in BOOKS:
            x = int(books.split('_')[-1])
            if x > current_book_id:
                current_book_id = x
    BOOKS[f'books_{current_book_id+1}'] = {'title': book_title,
                                           'author': book_author}
    return BOOKS[f'book_{current_book_id+1}']

@app.put("/{book_name}")
async def update_book(book_name:str,book_title:str,book_author:str):
    book_information ={'title':book_title,'author':book_author}
    BOOKS[book_name]=book_information
    return book_information


@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book {book_name} deleted'
