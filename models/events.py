from pydantic import BaseModel

from typing import List


class Event(BaseModel):
    id: int
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
