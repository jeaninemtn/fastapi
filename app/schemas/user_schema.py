"""
定義資料結構 (前端傳入資料 & 後端回傳資料 格式定義)
跟API相關

常使用 Pydantic 這個套件來建立模型（BaseModel），
用來進行資料的：
驗證（validation）
型別檢查（type checking）
自動轉換（例如 JSON ↔ Python object）
自動生成 OpenAPI 文件（Swagger UI）

"""

from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str