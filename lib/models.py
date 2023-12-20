from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel

Base = declarative_base()


# Define the Task model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class TaskCreate(BaseModel):
    title: str
    description: str
    status: bool


class TaskUpdate(BaseModel):
    title: str
    description: str
    status: bool


class TaskResponse(TaskCreate):
    id: int
    created_at: datetime