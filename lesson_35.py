#Lesson 35 — Pydantic: зачем сделали эту библиотеку, какие альтернативы есть, в чём проблема проверять данные руками.

from pydantic import BaseModel, ValidationError, Field
from typing import Literal

from pydantic import ValidationError

ERROR_MESSAGES = {
    "string_too_short": "Минимум {min_length} символа",
    "string_too_long": "Максимум {max_length} символов",
    "string_pattern_mismatch": "Только русские буквы и дефис",
    "greater_than": "Значение должно быть больше {gt}",
    "less_than": "Значение должно быть меньше {lt}",
    "literal_error": "Недопустимое значение из списка",
    "missing": "Обязательное поле",
    "int_parsing": "Введите целое число",
}

FIELD_NAMES = {
    "first_name": "Имя",
    "last_name": "Фамилия",
    "age": "Возраст",
    "status": "Статус",
}

class Employee(BaseModel):
    first_name: str = Field(
        min_length=2,
        max_length=50,
        pattern=r"^[А-Яа-яЁё-]+$"
    )
    last_name: str = Field(
        min_length=2,
        max_length=50,
        pattern=r"^[А-Яа-яЁё-]+$"
    )
    age: int = Field(
        gt=16,
        lt=80
    )
    status: Literal[
        "работает",
        "уволен",
        "отпуск",
        "кандидат"
    ] = "работает"


try:
    employee = Employee(
        first_name="Г",
        last_name="Дракула66",
        age=665,
        status="вампир"
    )

except ValidationError as e:
    for error in e.errors():
        # Захожу в loc конкретной ошибки, беру его и по этому названию из своего словаря беру человекочитаемое название поля
        field = FIELD_NAMES[error["loc"][0]]

        # Делаю это же с ошибкой (тип и сообщение)
        message = ERROR_MESSAGES.get(error["type"], error["msg"])

        message = message.format(**error.get("ctx", {}))
        print(f"{field} : {message}")