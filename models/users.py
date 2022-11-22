from pydantic import BaseModel, EmailStr
from typing import Optional, List

from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        schema_extra = {
            "example": {
                "email": "youemail@mail.ru",
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
