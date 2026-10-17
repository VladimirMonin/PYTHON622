#Lesson 35 — Pydantic: зачем сделали эту библиотеку, какие альтернативы есть, в чём проблема проверять данные руками.

from pydantic import BaseModel, ValidationError

class Employee(BaseModel):
    first_name: str
    last_name: str
    age: int

employee = Employee(
    first_name = "Граф",
    last_name = "Дракула",
    age = "665"
)
print(employee)
print(employee.age)
print(type(employee.age))

try:
    employee1 = Employee(
    first_name = "Прислужник",
    last_name = "Графа",
    age = "Нескажу"
)

except ValidationError as e:
    print(e)
    # print(e.__dict__)