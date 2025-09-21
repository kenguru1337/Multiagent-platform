from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="MultiAgent Platform API",
    version="0.1",
    description="Мультиагентная система для анализа и генерации отчётов"
)

# Роуты
app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
