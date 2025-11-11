# FastAPI Project

## Project Overview
This is a sample **FastAPI** project, featuring a basic folder structure and example routes.  
The project is designed following modern Python API development best practices, making it easy to quickly build RESTful APIs.

---

## Project Structure

```
app/
├─ main.py          # Entry point
├─ routers/         # API route modules
├─ models/          # SQLAlchemy models
├─ schemas/         # Pydantic data validation models
requirements.txt    # Project dependencies
README.md           # Project documentation
```

---

## Installation & Setup

1. **Create a virtual environment**
```
python -m venv venv
```

2. **Activate the virtual environment**
```
venv\Scripts\activate
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Running the Project**
```
fastapi dev main.py
```

5. **The server will run at**
```
http://127.0.0.1:8000
```
**Swagger API documentation is automatically available at:**
```
http://127.0.0.1:8000/docs
```

6. **Dependencies**
```
fastapi
uvicorn
(Optional) sqlalchemy, pydantic, pymysql, etc.
```