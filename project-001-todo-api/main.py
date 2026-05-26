from fastapi import FastAPI
from app.database.db import engine, Base

from app.routes import auth_routes
# from app.routes import todo_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
# app.include_router(todo_routes.router)


@app.get("/")
def home():
    return {"message": "Todo API Running"}