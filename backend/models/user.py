from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime, timezone

#user creation
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
#user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str
#mongodb user model
class UserDB(BaseModel):
    id: str = Field(default=None, alias="_id")
    email: str
    username: str
    hashed_password: str
    points: int = 50
    level: int = 1
    xp: int = 0
    buddy_name: str = 'study_bunny'
    active_theme: str = 'default'
    unlocked_themes : List[str] = Field(default_factory = list)
    unlocked_buddies : List[str] = Field(default_factory = list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

#user response (back to frontend)
class UserResponse(BaseModel):
    id: str
    email: str
    username: str
    points: int
    level: int
    xp: int
    buddy_name: str
    active_theme: str
    unlocked_themes : List[str]
    unlocked_buddies : List[str]