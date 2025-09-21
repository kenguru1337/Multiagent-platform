from src.multiagent.agents.report_agent import generate_report

def test_generate_report_contains_keywords():
    analysis_result = {
        "facts": ["AI используется в IDS"],
        "risks": ["False positive могут мешать работе"],
        "confidence": 0.9
    }
    report = generate_report(analysis_result)

    assert "Факты" in report
    assert "Риски" in report
    assert "Уверенность" in report
