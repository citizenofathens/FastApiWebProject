import sqlite3

from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates

app= FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id , symbol  FROM stock ORDER BY symbol
    """)

    rows = cursor.fetchall()
    return templates.TemplateResponse("index.html",{"request":request,"stocks":rows})