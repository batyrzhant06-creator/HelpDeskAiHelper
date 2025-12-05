# app/api/v1/stats.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.session import get_db
from app.models.ticket import Ticket, TicketStatus

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(func.count(Ticket.id)).scalar() or 0
    resolved = db.query(func.count(Ticket.id)).filter(Ticket.status == TicketStatus.resolved).scalar() or 0

    return {
        "total_tickets": total,
        "resolved_tickets": resolved,
    }
