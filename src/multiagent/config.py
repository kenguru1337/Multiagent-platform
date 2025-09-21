"""
config.py — конфигурация приложения.
Использует Pydantic BaseSettings для работы с переменными окружения.
"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "MultiAgent Platform"
    debug: bool = True
    log_level: str = "INFO"

    # Пример API ключа (для LLM или внешних сервисов)
    openai_api_key: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
