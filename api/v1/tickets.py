# app/api/v1/tickets.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketOut
from app.core.ai_stub import ai_core, TicketClassification

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("/ingest", response_model=TicketOut)
def ingest_ticket(ticket_in: TicketCreate, db: Session = Depends(get_db)):
    ticket = Ticket(
        source=ticket_in.source,
        subject=ticket_in.subject,
        body=ticket_in.body,
        language=ticket_in.language,
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    # Классификация через заглушку AI
    ticket_out = TicketOut.from_orm(ticket)
    classification = ai_core.classify_ticket(ticket_out)

    ticket.category = classification.category
    ticket.priority = classification.priority
    ticket.incident_type = classification.incident_type
    ticket.department = classification.department
    ticket.classification_confidence = classification.classification_confidence
    ticket.updated_at = datetime.utcnow()

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket


@router.get("/", response_model=List[TicketOut])
def list_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).order_by(Ticket.created_at.desc()).all()
    return tickets


@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: str, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket
