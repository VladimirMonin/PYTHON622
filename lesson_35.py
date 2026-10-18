#Lesson 35 — Pydantic: зачем сделали эту библиотеку, какие альтернативы есть, в чём проблема проверять данные руками.

from pydantic import BaseModel, ValidationError, Field
from typing import Annotated, Literal

from pydantic import ValidationError

# ERROR_MESSAGES = {
#     "string_too_short": "Минимум {min_length} символа",
#     "string_too_long": "Максимум {max_length} символов",
#     "string_pattern_mismatch": "Только русские буквы и дефис",
#     "greater_than": "Значение должно быть больше {gt}",
#     "less_than": "Значение должно быть меньше {lt}",
#     "literal_error": "Недопустимое значение из списка",
#     "missing": "Обязательное поле",
#     "int_parsing": "Введите целое число",
# }

# FIELD_NAMES = {
#     "first_name": "Имя",
#     "last_name": "Фамилия",
#     "age": "Возраст",
#     "status": "Статус",
# }

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

    is_married: bool

    hobbies: list[Annotated[str, Field(min_length=3, max_length=40)]] | None = Field(
    default=None,
    min_length=1,
    max_length=5
)


employee = Employee(
    first_name="Граф",
    last_name="Дракула",
    age="22",
    status="кандидат",
    is_married="No",
    hobbies=["Детишки", "Томатный сок, кхе, кхе!"]
)


# Преобразование в словарь
employee_dict = employee.model_dump()
print(employee_dict)

# Преобразование в JSON
employee_json = employee.model_dump_json(ensure_ascii=False, indent=2)
print(employee_json)

# Обратный перегон через методы model_vaidate и model_validate_json
employee_from_dict = Employee.model_validate(employee_dict)
employee_from_json = Employee.model_validate_json(employee_json)
