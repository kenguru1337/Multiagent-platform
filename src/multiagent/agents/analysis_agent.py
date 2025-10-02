# src/multiagent/agents/analysis_agent.py
from src.multiagent.utils.llm import llm


def analyze(query: str) -> dict:
    """Анализ запроса через LLM."""
    response = llm.ask(f"Проанализируй запрос и дай развернутый ответ: {query}")

    return {
        "query": query,
        "analysis": response
    }