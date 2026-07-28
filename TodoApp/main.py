from http.client import HTTPException
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status

import models

from models import Todos
from database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

class TodoRequest(BaseModel):
    title : str = Field(min_length=3)
    description : str = Field(min_length=5, max_length=200)
    priority : int = Field(gt=0 , le=15)
    complete : bool

@app.get("/")
async def read(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code= 404, detail= ' Todos not found yet, please try again and dont be stupet mather beach ')

@app.post("/todo/create", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest ):
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()


@app.put("/todo_update/{todo_id", status_code=status.HTTP_200_OK)
async def update_todo(db: db_dependency, todo_request: TodoRequest):
    pass