import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from lib.crud import TaskCRUD
from lib.database import SessionLocal, init_db
from lib.models import TaskCreate, TaskResponse

init_db()  # Initialize the database

app = FastAPI()


# Dependency to get the database session
def get_db():
    """
    Dependency to get the database session.

    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CRUD operations
crud = TaskCRUD()


@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.

    Args:
        task (TaskCreate): The task data.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        TaskResponse: The created task.
    """
    db_task = crud.create_task(db, title=task.title, description=task.description, status=False)
    return TaskResponse(**db_task.__dict__)


@app.get("/tasks/", response_model=list[TaskResponse])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Read a list of tasks.

    Args:
        skip (int, optional): Number of tasks to skip. Defaults to 0.
        limit (int, optional): Number of tasks to retrieve. Defaults to 10.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[TaskResponse]: List of tasks.
    """
    tasks = crud.read_tasks(db, skip=skip, limit=limit)
    return [TaskResponse(**task.__dict__) for task in tasks]


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Read a specific task by ID.

    Args:
        task_id (int): The task ID.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        TaskResponse: The requested task.
    """
    task = crud.read_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskResponse(**task.__dict__)


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate, status: bool, db: Session = Depends(get_db)):
    """
    Update a task by ID.

    Args:
        task_id (int): The task ID.
        task (TaskCreate): The task data for update.
        status (bool): The new status of the task.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        TaskResponse: The updated task.
    """
    updated_task = crud.update_task(db, task_id, title=task.title, description=task.description, status=bool(status))
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskResponse(**updated_task.__dict__)


@app.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task by ID.

    Args:
        task_id (int): The task ID.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        TaskResponse: The deleted task.
    """
    deleted_task = crud.delete_task(db, task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskResponse(**deleted_task.__dict__)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
