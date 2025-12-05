# app/main.py
from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

from app.api.v1 import tickets, assist, stats


def create_tables():
    Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI HelpDesk Backend",
    version="0.1.0",
)


@app.on_event("startup")
def on_startup():
    create_tables()


app.include_router(tickets.router)
app.include_router(assist.router)
app.include_router(stats.router)
