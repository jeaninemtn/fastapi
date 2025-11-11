from fastapi import FastAPI
from app.routers import users, projects
from app.database import Base, engine

# 建立資料表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MySQL Example")

# 建立路由
app.include_router(users.router)
app.include_router(projects.router)

@app.get("/")
def root():
    return {"message": "Hello FastAPI!"}
