"""
對照資料庫/定義資料庫的結構（table 結構）

Python(透過 ORM)描述資料庫的表格結構
不用直接寫SQL也能操作資料庫

"""

from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255), nullable=False)