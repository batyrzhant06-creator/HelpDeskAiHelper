# app/schemas/assist.py
from typing import List, Optional
from pydantic import BaseModel


class SimilarCase(BaseModel):
    ticket_id: str
    summary: str
    resolution: Optional[str] = None


class AssistResponse(BaseModel):
    summary: str
    suggested_reply: str
    alternatives: List[str] = []
    similar_cases: List[SimilarCase] = []
    translations: dict = {}
