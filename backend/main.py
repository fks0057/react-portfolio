import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    completed = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    completed: bool


@app.get("/")
def home():
    return {"message": "Backend is running with MySQL Todo App"}


@app.get("/todos")
def get_todos():
    db = SessionLocal()
    try:
        todos = db.query(Todo).order_by(Todo.id).all()
        return {
            "todos": [
                {
                    "id": todo.id,
                    "title": todo.title,
                    "completed": todo.completed,
                }
                for todo in todos
            ]
        }
    finally:
        db.close()


@app.post("/todos")
def create_todo(todo: TodoCreate):
    db = SessionLocal()
    try:
        new_todo = Todo(title=todo.title, completed=False)
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)

        return {
            "id": new_todo.id,
            "title": new_todo.title,
            "completed": new_todo.completed,
        }
    finally:
        db.close()


@app.patch("/todos/{todo_id}")
def update_todo(todo_id: int, todo_update: TodoUpdate):
    db = SessionLocal()
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()

        if todo is None:
            return {"error": "Todo not found"}

        todo.completed = todo_update.completed
        db.commit()
        db.refresh(todo)

        return {
            "id": todo.id,
            "title": todo.title,
            "completed": todo.completed,
        }
    finally:
        db.close()


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    db = SessionLocal()
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id).first()

        if todo is None:
            return {"error": "Todo not found"}

        db.delete(todo)
        db.commit()

        return {"message": "Todo deleted"}
    finally:
        db.close()