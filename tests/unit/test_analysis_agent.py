
from src.multiagent.agents.analysis_agent import analyze



def test_analyze_returns_expected_structure():
    docs = ["AI используется в IDS", "False positive могут мешать работе"]
    result = analyze(docs)

    assert "facts" in result
    assert "risks" in result
    assert "confidence" in result

    assert isinstance(result["facts"], list)
    assert isinstance(result["risks"], list)
    assert isinstance(result["confidence"], float)
