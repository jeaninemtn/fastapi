from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str = None  # description 可以不填

class ProjectUpdate(BaseModel):
    name: str = None
    description: str = None

class ProjectRead(BaseModel):
    id: int
    name: str
    description: str = None

    class Config:
        orm_mode = True
