from beanie import Document
from pydantic import BaseModel
from typing import Optional, List


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "How to make rasengan",
                "image": "https://jut.su/rasengan.png",
                "description": "Learning jutsu from Naruto anime",
                "tags": ["Naruto", "Konoha", "Ninja"],
                "location": "Discord"
            }
        }

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "How to make rasengan",
                "image": "https://jut.su/rasengan.png",
                "description": "Learning jutsu from Naruto anime",
                "tags": ["Naruto", "Konoha", "Ninja"],
                "location": "Discord"
            }
        }
