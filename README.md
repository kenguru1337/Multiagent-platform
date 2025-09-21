# 🤖 MultiAgent Platform

## 📌 Описание
`MultiAgent Platform` — это прототип мультиагентной системы на базе **FastAPI**, **LangChain** и **Python**, которая автоматизирует обработку запросов.  
Система использует несколько агентов:

- 🔎 **Search Agent** — ищет релевантную информацию  
- 📊 **Analysis Agent** — анализирует найденные данные (NER, sentiment, классификация)  
- 📝 **Report Agent** — формирует итоговый человекочитаемый отчёт  

Архитектура позволяет легко расширять систему новыми агентами (например, Risk Agent, Pentest Agent) и интегрировать её в DevSecOps-процессы.

---

## 🏗 Архитектура
```text
Запрос пользователя
        │
        ▼
   [FastAPI API]  ← POST /process/
        │
        ▼
 ┌───────────────┐
 │ Orchestrator  │ — управляет пайплайном
 └───────────────┘
   │      │      │
   ▼      ▼      ▼
Search   Analysis  Report
 Agent    Agent     Agent
   │       │        │
   └──────►└───────►└───▶ Итоговый отчёт (JSON + текст)
```

## 🚀 Возможные сценарии использования
### **Кибербезопасность**

Автоматизация поиска CVE и формирование отчётов о рисках для DevSecOps-команд.
### **Аналитика данных**

Поиск и анализ научных публикаций или статей об AI/ML с краткими выводами.
### **Бизнес-аналитика**

Генерация сжатых обзоров рынка или трендов на основе открытых данных.
### **Интеграция в CI/CD**

Автоматическая проверка зависимостей проекта на наличие уязвимостей с генерацией отчёта.

### 🛠 Стек технологий
* Python 3.10+
* FastAPI / Pydantic
* LangChain
* Transformers (HuggingFace)
* FAISS / Chroma (векторное хранилище)
* Docker, docker-compose
* GitHub Actions (CI/CD)
* Pytest, flake8, bandit

## 📂 Структура проекта
```
multiagent-platform/
│
├── .github/
│   └── workflows/
│       ├── ci.yml             # CI/CD пайплайн: тесты, линтер, security
│       └── docker-build.yml   # Билд и публикация Docker-образа
│
├── docker/
│   ├── Dockerfile             # Сборка образа FastAPI приложения
│   └── docker-compose.yml     # Запуск API + (в будущем) ChromaDB/FAISS
│
├── docs/
│   ├── architecture.md        # Подробное описание архитектуры
│   └── use_cases.md           # Сценарии применения
│
├── src/
│   └── multiagent/
│       ├── api/               # REST API (FastAPI)
│       │   ├── main.py        # Точка входа приложения
│       │   ├── routes.py      # Эндпоинты API
│       │   └── schemas.py     # Pydantic-модели запросов/ответов
│       │
│       ├── agents/            # Агенты мультиагентной системы
│       │   ├── search_agent.py    # Поиск информации
│       │   ├── analysis_agent.py  # Анализ документов
│       │   ├── report_agent.py    # Генерация отчёта
│       │   └── orchestrator.py    # Управляет пайплайном агентов
│       │
│       ├── db/                # Работа с хранилищем (будущее расширение)
│       │   └── vector_store.py    # FAISS / ChromaDB для эмбеддингов
│       │
│       ├── utils/             # Утилиты
│       │   ├── prompts.py         # Шаблоны промптов для LLM
│       │   └── embeddings.py      # Генерация эмбеддингов
│       │
│       ├── config.py          # Конфигурация проекта (pydantic.BaseSettings)
│       └── logging_conf.py    # Логирование
│
├── tests/                     # Тесты
│   ├── unit/                  # Юнит-тесты (агенты)
│   │   ├── test_search_agent.py
│   │   ├── test_analysis_agent.py
│   │   └── test_report_agent.py
│   └── integration/           # Интеграционные тесты API
│       └── test_api.py
│
├── .env.example               # Пример переменных окружения
├── requirements.txt           # Зависимости Python
├── README.md                  # Документация проекта
└── LICENSE                    # Лицензия (MIT/Apache 2.0)
```

## 🚀 Запуск проекта
1. **Клонировать репозиторий**
```
git clone https://github.com/username/multiagent-platform.git
cd multiagent-platform
```
2. **Установить зависимости**
```
pip install -r requirements.txt
```
3. **Запуск локально**
```
uvicorn src.multiagent.api.main:app --reload
API будет доступно по адресу: http://localhost:8000/docs
```
4. **Запуск через Docker**
```
docker-compose up --build
```

## 📡 Пример запроса
```
POST /process/
{
  "query": "AI в кибербезопасности"
}

Ответ

{
  "query": "AI в кибербезопасности",
  "report": "AI активно используется для IDS, помогает анализировать сетевые логи...",
  "insights": {
    "facts": ["AI используется в IDS", "Нейросети помогают в анализе логов"],
    "risks": ["False positive при обнаружении аномалий"],
    "confidence": 0.87
  }
}
```

### ✅ DevSecOps практики
* 🧪 Автотесты (pytest)
* 🔍 Линтер (flake8)
* 🔒 Security scan (bandit, pip-audit)
* 🐳 Контейнеризация (Docker, docker-compose)
* ⚡ CI/CD (GitHub Actions)

### 📈 MVP реализует
1. Взаимодействие агентов через orchestrator
2. REST API для внешних сервисов
3. Контейнеризацию и CI/CD
4. Минимальные DevSecOps-практики