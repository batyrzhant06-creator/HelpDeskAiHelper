# app/models/ticket.py
import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Enum, Float, Boolean
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from app.db.base import Base
import enum


def gen_uuid():
    return str(uuid.uuid4())


class TicketStatus(str, enum.Enum):
    new = "new"
    in_progress = "in_progress"
    resolved = "resolved"
    waiting_user = "waiting_user"
    escalated = "escalated"


class TicketPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(String, primary_key=True, default=gen_uuid, index=True)

    source = Column(String, nullable=False)  # email|chat|portal|phone
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)

    language = Column(String, nullable=True)  # ru|kk|en|auto

    # Классификация
    category = Column(String, nullable=True)        # network|access|hardware|software|other
    priority = Column(Enum(TicketPriority), nullable=True)
    incident_type = Column(String, nullable=True)   # incident|request|question|bug
    department = Column(String, nullable=True)
    classification_confidence = Column(Float, nullable=True)

    status = Column(Enum(TicketStatus), default=TicketStatus.new, nullable=False)

    auto_resolved = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
