# app/core/config.py
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:Abdigappar0328%21%40%23@localhost:3306/helpdesk",
)
