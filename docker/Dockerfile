FROM python:3.10-slim

# Рабочая директория
WORKDIR /app

# Установим зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходники
COPY src/ ./src

# Запускаем FastAPI через Uvicorn
CMD ["uvicorn", "src.multiagent.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
