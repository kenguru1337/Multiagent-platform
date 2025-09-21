from .search_agent import search
from .analysis_agent import analyze
from .report_agent import generate_report



def run_pipeline(query: str):
    """
    Оркестратор связывает работу агентов.
    """
    # 1. Поиск информации
    docs = search(query)

    # 2. Анализ найденного
    analysis_result = analyze(docs)

    # 3. Формирование отчёта
    report = generate_report(analysis_result)

    return {
        "query": query,
        "report": report,
        "insights": {
            "facts": analysis_result["facts"],
            "risks": analysis_result["risks"]
        },
        "confidence": analysis_result["confidence"]
    }
