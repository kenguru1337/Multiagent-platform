# src/multiagent/agents/orchestrator.py
from src.multiagent.agents.analysis_agent import analyze
from src.multiagent.agents.report_agent import generate_report


def process_query(query: str) -> dict:
    """Основной пайплайн: анализ -> отчет."""
    analysis_result = analyze(query)
    report = generate_report(query, analysis_result["analysis"])
    return report
