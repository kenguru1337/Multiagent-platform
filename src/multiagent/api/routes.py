from fastapi import APIRouter
from .schemas import QueryRequest, QueryResponse
from ..agents.orchestrator import run_pipeline

router = APIRouter()

@router.post("/process", response_model=QueryResponse)


def process_query(request: QueryRequest):
    result = run_pipeline(request.query)
    return result
