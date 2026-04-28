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