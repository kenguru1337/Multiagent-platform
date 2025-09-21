def analyze(documents):
    """
    Базовый анализ документов.
    На данном этапе просто выделяем факты и риски.
    """
    facts = []
    risks = []

    for doc in documents:
        facts.append(doc)
        if "False positive" in doc:
            risks.append(doc)

    confidence = 0.9
    return {"facts": facts, "risks": risks, "confidence": confidence}
