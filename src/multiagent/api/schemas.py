from pydantic import BaseModel
from typing import List, Dict



class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    query: str
    report: str
    insights: Dict[str, List[str]]
    confidence: float
