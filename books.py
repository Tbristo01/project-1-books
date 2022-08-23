from enum import Enum
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


@app.get('/')
async def read_all_book():
    return BOOKS


@app.get('/books/mybook')
async def read_favorite_book():
    return {'book_title': 'My favorite book '}


@app.get('/books/{book_id}')
async def read_book(book_id: int):
    return {'book_id': book_id}

@app.get('directions/{direction_name}')
async def get_direction(direction_name:DirectionName):
    if direction_name == DirectionName.north:
        return{'Direction': direction_name, 'sub':'up'}
    if direction_name == DirectionName.south:
        return{'Direction': direction_name, 'sub':'down'}
    if direction_name == DirectionName.east:
        return{'Direction': direction_name, 'sub':'left'}
    if direction_name == DirectionName.west:
        return{'Direction': direction_name, 'sub':'right'}
    
@app.get("/book_name}")
async def read_book(book_name:str):
    return BOOKS[book_name]