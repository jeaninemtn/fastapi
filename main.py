# FastAPI
# ASGI Server (Uvicorn)
# ASGI(Asynchronous Server Gateway Interface)

# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}