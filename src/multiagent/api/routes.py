# src/multiagent/api/routes.py
from fastapi import APIRouter
from src.multiagent.api.schemas import QueryRequest, QueryResponse
from src.multiagent.agents.orchestrator import process_query

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/process", response_model=QueryResponse)
async def process_query_route(request: QueryRequest):
    return process_query(request.query)
