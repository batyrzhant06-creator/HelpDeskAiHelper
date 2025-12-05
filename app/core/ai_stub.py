# app/core/ai_stub.py
from typing import List
from app.schemas.ticket import TicketOut, TicketClassification
from app.schemas.message import MessageOut
from app.schemas.assist import AssistResponse, SimilarCase


class AICoreStub:
    def classify_ticket(self, ticket: TicketOut) -> TicketClassification:
        # TODO: заменить на реальный вызов LLM
        return TicketClassification(
            category="other",
            priority="medium",
            incident_type="question",
            department="IT-ServiceDesk",
            classification_confidence=0.5,
        )

    def build_assist_response(
        self,
        ticket: TicketOut,
        messages: List[MessageOut],
    ) -> AssistResponse:
        return AssistResponse(
            summary=f"Пользователь сообщает: {ticket.subject}",
            suggested_reply="Здравствуйте! Мы получили вашу заявку и приступили к её обработке.",
            alternatives=[
                "Здравствуйте! Спасибо за обращение, мы проверим описанную проблему и вернёмся с ответом.",
                "Добрый день! Ваша заявка принята, сейчас уточним детали и сообщим решение.",
            ],
            similar_cases=[
                SimilarCase(
                    ticket_id="demo-1",
                    summary="Похожая проблема с доступом к сервису",
                    resolution="Перевыпуск прав доступа и перезагрузка сервиса",
                )
            ],
            translations={
                "summary_ru": f"Пользователь сообщает: {ticket.subject}",
                "summary_kk": "Пайдаланушы осыған ұқсас мәселе туралы хабарлады.",
            },
        )


ai_core = AICoreStub()
