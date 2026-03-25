from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import engine, Base, get_db
from app.models import Task

app = FastAPI()

Base.metadata.create_all(bind=engine)


class TaskCreate(BaseModel):
    title: str
    completed: bool

class TaskResponse(BaseModel):
    title: str
    completed: bool


tasks = []

@app.get("/")
def read_root():
    return {"message": "First API"}

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    
    return tasks

@app.post("/tasks")
def create_task(title: str, db: Session = Depends(get_db)):
    new_task = Task(title=title)
    
    db.add(new_task)
    db.commit()
    db.fefresh(new_task)
    
    return new_task

