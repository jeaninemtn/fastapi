from pydantic import BaseModel
from typing import Optional

class ProjectCreate(BaseModel):
    name: str
    description: str = None

class ProjectUpdate(BaseModel):
    name: str = None
    description: str = None

class ProjectRead(BaseModel):
    id: int
    name: str
    description: str = None
    user_id: int

    class Config:
        orm_mode = True
