# app/schemas/message.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MessageBase(BaseModel):
    author_type: str
    body: str
    language: Optional[str] = None


class MessageCreate(MessageBase):
    ticket_id: str


class MessageOut(MessageBase):
    id: str
    ticket_id: str
    created_at: datetime

    class Config:
        orm_mode = True
