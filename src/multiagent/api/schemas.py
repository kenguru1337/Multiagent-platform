# src/multiagent/api/schemas.py
from pydantic import BaseModel
from typing import List


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    query: str
    report: str
    insights: List[str]
    confidence: float
