from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from typing import Optional, List

from models.events import Event


class User(Document):
    email: EmailStr
    username: str
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "youemail@mail.ru",
                "username": "Madara",
                "password": "cool_password",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "youemail@mail.ru",
                "password": "strong_password"
            }
        }
