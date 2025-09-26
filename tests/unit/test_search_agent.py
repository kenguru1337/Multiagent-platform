
from multiagent.agents.search_agent import search


def test_search_returns_documents():
    query = "AI в безопасности"
    docs = search(query)
    assert isinstance(docs, list)
    assert len(docs) > 0
    assert all(isinstance(d, str) for d in docs)
