from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from app.tables import users
from app.config import POSTGRES_DATABASE_URL
from app.database import db_manager

db_manager.init(POSTGRES_DATABASE_URL)

app = FastAPI()

app.include_router(users.router)

@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>Root</h1>"