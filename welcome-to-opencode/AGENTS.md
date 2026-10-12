# Project Agent Guide

## Project Overview
Python-сервис для <краткое описание>. Python 3.12+, зависимости через `uv`.

## Commands

### Setup
- Install deps: `uv sync`
- Activate venv: `.venv/bin/activate`

### Development
- Run app: `uv run python -m app.main`
- Run tests: `uv run pytest`
- Single test: `uv run pytest tests/test_module.py::test_function`
- Coverage: `uv run pytest --cov=app --cov-report=term-missing`

### Quality
- L`uv run ruff check .`
- Format: `int: uv run ruff format .`
- Type check: `uv run mypy app/`

## Architecture
- `src/app/` — исходный код приложения
- `src/app/api/` — FastAPI-роутеры: валидация + вызов сервисов
- `src/app/services/` — бизнес-логика, не зависит от HTTP
- `src/app/repositories/` — работа с БД через SQLAlchemy
- `src/app/models/` — Pydantic-схемы и ORM-модели
- `src/app/core/` — конфиг, логирование, безопасность
- `tests/` — pytest, общие фикстуры в `conftest.py`

## Conventions

### Code Style
- Форматирование: `ruff format`, длина строки 100
- Линтер: `ruff check`, конфиг в `pyproject.toml`
- Типизация: обязательна для всех публичных функций и методов
- Импорты: абсолютные внутри пакета

### Python Idioms
- `pathlib.Path` вместо `os.path`
- f-strings вместо `.format()` и `%`
- `dataclass` или Pydantic вместо «голых» dict
- Async: `async def` для I/O, синхронный код для CPU-bound
- Исключения: свои классы наследовать от `AppError` в `app.core.exceptions`

### Docstrings
- Для написания и обновления docstring использовать скилл `docstring-writer`

### Testing
- Фреймворк: pytest + pytest-asyncio
- Фикстуры: в `tests/conftest.py`, область видимости по умолчанию — `function`
- Моки: `pytest-mock`, не `unittest.mock` напрямую
- Именование: `test_<что>_<при_каких_условиях>_<ожидаемый_результат>`

## Skills
- **`docstring-writer`** — для написания и обновления docstring. Использовать всегда, когда нужно документировать функцию, класс или модуль.

## Notes
- Не коммитить `.env`, использовать `.env.example`
- Миграции: `uv run alembic revision --autogenerate -m "message"`, применение: `uv run alembic upgrade head`
- Логи: `structlog`, конфиг в `app.core.logging`