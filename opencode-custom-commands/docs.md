---
description: Update README and add/refresh docstrings across the project
agent: build
model: opencode/muse-spark-1.3-contributor-free
---

Analyze the project and perform the following documentation tasks. Your ENTIRE response must be written in Russian. Only code identifiers (class names, function names, variable names, file paths, type names) must remain in their original form.

You MUST proactively read any files you need to complete the tasks below.

## Task 1: Update README.md
Read the existing README.md file (if it exists). If it doesn't exist, do not create it.
Update the README.md with the following sections:
- **Название проекта** и краткое описание.
- **Стек технологий** (языки, фреймворки, библиотеки).
- **Установка** (команды для установки зависимостей).
- **Запуск** (команды для запуска в dev и prod режимах).
- **Структура проекта** (дерево ключевых директорий и файлов с описанием).
- **Примеры использования** (если применимо).

Base the README content on actual analysis of the project files. Do not invent information.

## Task 2: Add/Update Docstrings

Go through ALL source code files in the project and add or update docstrings for all public and private classes, methods, and functions.

### Строгий шаблон docstring (обязателен к соблюдению)

Используй ТОЛЬКО следующий стиль docstrings. Отступления недопустимы.

## Модуль

```python
"""Краткое описание модуля в одном предложении.

Подробное описание, если нужно.
"""
```

## Класс

```python
class ClassName:
    """Краткое описание класса.

    Attributes:
        attr1: Описание атрибута.
        attr2: Описание атрибута.
    """
```

## Функция

```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """Краткое описание в повелительном наклонении.

    Подробное описание (опционально).

    params:
        param1: Описание первого параметра.
        param2: Описание второго параметра.

    returns:
        Описание возвращаемого значения.

    raises:
        ErrorType: Когда выбрасывается.
    """
```

## Асинхронная функция

```python
async def async_function(param: Type) -> ReturnType:
    """Краткое описание.

    params:
        param: Описание.

    returns:
        Описание.
    """
```

## Приватная функция

```python
def _private_function(param: Type) -> ReturnType:
    """Краткое описание в одну строку."""
```

## Edge cases

- **Нет параметров**: секция `params` опускается.
- **Ничего не возвращает**: секция `returns` опускается.
- **Ничего не выбрасывает**: секция `raises` опускается.
- **Генератор**: `yields:` вместо `returns:`.
- **property**: docstring описывает возвращаемое значение, без `params`.
- **`__init__`**: описывать `params`, не описывать `returns`.

## Чек-лист

- [ ] Краткое описание с точкой в конце.
- [ ] Пустая строка перед подробным описанием.
- [ ] `params` для всех параметров.
- [ ] `returns` только если есть возврат.
- [ ] `raises` для всех явно выбрасываемых исключений.
- [ ] Без дублирования типов.

## Правила применения к другим языкам

Для языков, отличных от Python, используй наиболее близкий по смыслу эквивалент того же стиля:

JavaScript/TypeScript: JSDoc с секциями @param, @returns, @throws.
Java: Javadoc с @param, @return, @throws.
Go: Go doc comments в том же структурном стиле.
Другие языки: наиболее распространённый в этом языке формат, максимально повторяющий логику шаблона выше.

IMPORTANT: Docstrings пишутся на русском языке (описания и пояснения), но идентификаторы кода (имена классов, функций, переменных, типов, путей) остаются в оригинальном виде. НЕ изменяй логику кода — только добавляй или обновляй docstrings. Если docstring уже существует и соответствует шаблону — оставь его без изменений. Обновляй только те, что отсутствуют, неполные или не соответствуют шаблону. Пропускай автогенерируемые файлы, конфигурационные файлы и файлы без осмысленного кода для документирования.

После выполнения обеих задач предоставь краткое резюме изменений на русском языке.