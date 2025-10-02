# src/multiagent/api/main.py
from fastapi import FastAPI
from src.multiagent.api.routes import router

app = FastAPI(title="Multiagent Platform with LLM")

app.include_router(router)
