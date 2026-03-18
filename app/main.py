from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: TaskCreate):
    tasks.append(task.model_dump())
    return {"message": "Task created"}

