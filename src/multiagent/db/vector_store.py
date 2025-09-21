"""
vector_store.py — модуль для хранения и поиска векторов.
Сейчас фейковая реализация, позже можно подключить FAISS или Chroma.
"""


class VectorStore:
    def __init__(self):
        self.vectors = []

    def add(self, text: str, embedding: list):
        self.vectors.append((text, embedding))

    def search(self, query_embedding: list, top_k: int = 3):
        # Пока возвращаем все сохранённые тексты
        return [text for text, _ in self.vectors][:top_k]


# Глобальный объект (как singleton)
vector_store = VectorStore()
