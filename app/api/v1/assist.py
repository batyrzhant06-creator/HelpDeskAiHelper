# app/api/v1/assist.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.ticket import Ticket
from app.models.message import Message
from app.schemas.ticket import TicketOut
from app.schemas.message import MessageOut
from app.schemas.assist import AssistResponse
from app.core.ai_stub import ai_core

router = APIRouter(prefix="/assist", tags=["assist"])


@router.get("/operator/{ticket_id}", response_model=AssistResponse)
def assist_operator(ticket_id: str, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    messages = (
        db.query(Message)
        .filter(Message.ticket_id == ticket_id)
        .order_by(Message.created_at.asc())
        .all()
    )

    ticket_out = TicketOut.from_orm(ticket)
    messages_out: List[MessageOut] = [MessageOut.from_orm(m) for m in messages]

    assist_response = ai_core.build_assist_response(ticket_out, messages_out)
    return assist_response
