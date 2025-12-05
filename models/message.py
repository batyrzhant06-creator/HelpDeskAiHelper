# app/models/message.py
import uuid

from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.ticket import Ticket


class Message(Base):
    __tablename__ = "ticket_messages"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    ticket_id = Column(String, ForeignKey("tickets.id"), nullable=False, index=True)

    author_type = Column(String, nullable=False)  # user|operator|system
    language = Column(String, nullable=True)
    body = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    ticket = relationship("Ticket", backref="messages")
