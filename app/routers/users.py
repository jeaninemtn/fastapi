from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserRead, UserLogin

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Dependency: 取得資料庫 session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 取得所有使用者
@router.get("/", response_model=List[UserRead])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# 新增使用者
@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # TODO password 加密
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 根據 ID 取得使用者
@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 刪除使用者
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()

    return {"message": "User deleted successful", "username": user.username }

# 登入
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.password != db_user.password:
        raise HTTPException(status_code=401, detail="Invalid username or password") 
    
    return {"message": "Login successful", "user_id": db_user.id}
