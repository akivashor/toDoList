from typing import Type, Optional

from sqlalchemy.orm import Session

from lib.models import Task


class TaskCRUD:
    def create_task(self, db: Session, title: str, description: str, status: bool) -> Task:
        db_task = Task(title=title, description=description, status=status)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    def read_tasks(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Task).offset(skip).limit(limit).all()

    def read_task(self, db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    def update_task(self, db: Session, task_id: int, title: str, description: str, status: Optional[bool]) -> Task:
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if db_task:
            db_task.title = title
            db_task.description = description
            db_task.status = status
            db.commit()
            db.refresh(db_task)
        return db_task

    def delete_task(self, db: Session, task_id: int) -> Type[Task] | None:
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if db_task:
            db.delete(db_task)
            db.commit()
        return db_task
