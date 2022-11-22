from typing import Optional, List

from sqlmodel import JSON, SQLModel, Field, Column


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "How to make rasengan",
                "image": "https://jut.su/rasengan.png",
                "description": "Learning jutsu from Naruto anime",
                "tags": ["Naruto", "Konoha", "Ninja"],
                "location": "Discord"
            }
        }


class EventUpdate(SQLModel):
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

