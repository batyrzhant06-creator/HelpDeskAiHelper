# app/schemas/ticket.py
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

from app.models.ticket import TicketStatus, TicketPriority


class TicketBase(BaseModel):
    source: str
    subject: str
    body: str
    language: Optional[str] = "auto"


class TicketCreate(TicketBase):
    pass


class TicketClassification(BaseModel):
    category: Optional[str] = None
    priority: Optional[TicketPriority] = None
    incident_type: Optional[str] = None
    department: Optional[str] = None
    classification_confidence: Optional[float] = None


class TicketUpdate(BaseModel):
    status: Optional[TicketStatus] = None
    classification: Optional[TicketClassification] = None


class TicketOut(BaseModel):
    id: str
    source: str
    subject: str
    body: str
    language: Optional[str]

    category: Optional[str]
    priority: Optional[TicketPriority]
    incident_type: Optional[str]
    department: Optional[str]
    classification_confidence: Optional[float]

    status: TicketStatus
    auto_resolved: bool

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
