import uuid
from datetime import datetime
import enum

from sqlalchemy import Column, String, DateTime, Enum, Float, Boolean, Text

from app.db.base import Base


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

    # UUID как строка – 36 символов
    id = Column(String(36), primary_key=True, default=gen_uuid, index=True)

    # Короткие строки → VARCHAR с длиной
    source = Column(String(50), nullable=False)          # email|chat|portal|phone
    subject = Column(String(255), nullable=False)

    # Длинный текст → Text (в MySQL это TEXT)
    body = Column(Text, nullable=False)

    language = Column(String(10), nullable=True)         # ru|kk|en|auto

    category = Column(String(50), nullable=True)
    incident_type = Column(String(50), nullable=True)
    department = Column(String(100), nullable=True)

    classification_confidence = Column(Float, nullable=True)

    status = Column(Enum(TicketStatus), default=TicketStatus.new, nullable=False)

    auto_resolved = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
