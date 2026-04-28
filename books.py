from fastapi import Body,FastAPI

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
    
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{books_author}/")
async def read_author_category_by_query(book_author:str,category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
        book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
    
