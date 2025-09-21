

def generate_report(analysis_result):
    """
    Генерация текстового отчёта на основе анализа.
    """
    facts = analysis_result["facts"]
    risks = analysis_result["risks"]

    report = "Отчёт по запросу:\n"
    report += "- Факты:\n" + "\n".join(f"- {f}" for f in facts) + "\n"

    if risks:
        report += "- Риски:\n" + "\n".join(f"- {r}" for r in risks) + "\n"

    report += f"Уверенность анализа: {analysis_result['confidence']}"
    return report
