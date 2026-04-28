from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'title': 'Title One','author':'author One','category':'science'},
    {'title': 'Title Two','author':'author Two','category':'science'},
    {'title': 'Title Three','author':'author Three','category':'history'},
    {'title': 'Title Four','author':'author Four','category':'math'},
    {'title': 'Title Five','author':'author Five','category':'math'},
    {'title': 'Title Six','author':'author Two','category':'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title :str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
