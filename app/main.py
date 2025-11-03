from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes import users, notes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Notes API")

app.include_router(users.router)
app.include_router(notes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI User Notes API!"}
