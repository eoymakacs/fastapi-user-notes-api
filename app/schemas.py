# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Define Pydantic schemas for request and response validation.

# ----- USER SCHEMAS -----
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

# ----- NOTE SCHEMAS -----
class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
