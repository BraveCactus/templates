# Error Handling Guidelines

Правила обработки исключений в проекте. Применяются ко всем модулям,
кроме тестов и скриптов одноразового использования.

## 1. Иерархия исключений

Все доменные исключения наследуются от `AppError` из `app.core.exceptions`.

```python
class AppError(Exception):
    """Базовое исключение приложения."""


class UserNotFoundError(AppError):
    """Пользователь не найден."""


class RepositoryError(AppError):
    """Ошибка при обращении к хранилищу данных."""
```

**Запрещено**:
- Наследоваться напрямую от `Exception` в доменном коде.
- Создавать исключения без docstring.
- Использовать `raise Exception("...")` или `raise RuntimeError("...")` в бизнес-логике.

## 2. Когда выбрасывать, а когда возвращать

- **Выбрасывать**: если ситуация нарушает контракт функции и вызывающий код не может её игнорировать (`UserNotFoundError`, `ValidationError`).
- **Возвращать `None` или `Result`**: если отсутствие значения — нормальный сценарий (`find_user` может вернуть `None`).
- **Не выбрасывать**: для управления потоком исполнения. Исключение — это не `if/else`.

```python
# Правильно: отсутствие — нормальный сценарий
def find_user(self, user_id: int) -> User | None:
    """Возвращает пользователя или None, если не найден."""
    return self.repo.find(user_id)


# Правильно: нарушение контракта — исключение
def get_user(self, user_id: int) -> User:
    """Возвращает пользователя. Выбрасывает UserNotFoundError, если не найден."""
    user = self.repo.find(user_id)
    if user is None:
        raise UserNotFoundError(f"User {user_id} not found")
    return user
```

## 3. Обработка на границах

- **В сервисах**: не ловить исключения репозиториев, если нечего добавить.
- **В API-роутерах**: ловить доменные исключения и преобразовывать в HTTP-ответы.
- **В фоновых задачах**: ловить всё, логировать и продолжать, чтобы не убить воркер.

```python
# Правильно: обработка на границе API
@router.get("/users/{user_id}")
async def get_user(user_id: int, service: UserService = Depends()) -> UserResponse:
    try:
        user = await service.get_user(user_id)
    except UserNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return UserResponse.from_orm(user)
```

```python
# Неправильно: глотание исключений в сервисе
def get_user(self, user_id: int) -> User:
    try:
        return self.repo.find(user_id)
    except Exception:
        pass  # ← молча теряем ошибку
```

## 4. `raise ... from ...`

Всегда указывайте исходное исключение через `from`, если перевыбрасываете.

```python
# Правильно
try:
    data = json.loads(raw)
except json.JSONDecodeError as exc:
    raise ValidationError("Invalid JSON payload") from exc

# Неправильно: теряем контекст
try:
    data = json.loads(raw)
except json.JSONDecodeError:
    raise ValidationError("Invalid JSON payload")
```

## 5. Логирование

- Логировать исключение **один раз** — на границе, где оно обрабатывается.
- Использовать `logger.exception(...)` внутри `except`, чтобы попал traceback.
- Не логировать и не выбрасывать одновременно (иначе двойные записи).

```python
# Правильно
except RepositoryError:
    logger.exception("Failed to fetch user", extra={"user_id": user_id})
    raise
```

## 6. Что запрещено

- `except Exception: pass` — молчаливое проглатывание.
- `except:` без типа — ловит даже `KeyboardInterrupt`.
- Ловить `BaseException` без веской причины.
- Использовать исключения для ветвления (`try/except` вместо `if`).
- Хранить в исключении чувствительные данные (пароли, токены).

## 7. Чек-лист

- [ ] Доменное исключение наследуется от `AppError`.
- [ ] У исключения есть docstring.
- [ ] `raise ... from ...` при перевыбрасывании.
- [ ] Обработка на границе, а не в глубине.
- [ ] Логирование ровно один раз.
- [ ] Нет `except Exception: pass` и голых `except:`.
- [ ] В сообщении исключения нет секретов.