from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models.project import Project
from app.schemas.project_schema import ProjectCreate, ProjectRead, ProjectUpdate

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all projects
@router.get("/", response_model=List[ProjectRead])
def get_projects(db: Session = Depends(get_db), current_user_id: int = 1):
    return db.query(Project).filter(Project.user_id == current_user_id).all()

# POST create project
@router.post("/", response_model=ProjectRead)
def create_project(project: ProjectCreate, db: Session = Depends(get_db), current_user_id: int = 1):  # TODO: 登入機制
    new_project = Project(
        name=project.name,
        description=project.description,
        user_id=current_user_id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

# GET project detail
@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# PUT edit project
@router.put("/{project_id}", response_model=ProjectRead)
def update_project(project_id: int, project_update: ProjectUpdate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if project_update.name is not None:
        project.name = project_update.name
    if project_update.description is not None:
        project.description = project_update.description
    db.commit()
    db.refresh(project)
    return project

# DELETE project
@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}
