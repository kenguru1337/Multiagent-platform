# src/multiagent/agents/report_agent.py
def generate_report(query: str, analysis: str) -> dict:
    """Генерация отчета по результатам анализа."""
    return {
        "query": query,
        "report": f"Отчет по запросу '{query}': {analysis}",
        "insights": ["LLM сгенерировала инсайт", "Можно улучшить промпт"],
        "confidence": 0.85  # условно, можно считать уверенность через метрики
    }
