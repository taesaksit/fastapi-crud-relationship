from fastapi import FastAPI, HTTPException
from .database import Base, engine
from .routers import category
from .utils.exception_handlers import http_exception_handler

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.add_exception_handler(HTTPException,http_exception_handler)
app.include_router(category.router)

@app.get("/")
def root():
    return {"message":"FastAPI-CRUD-Relation database"}