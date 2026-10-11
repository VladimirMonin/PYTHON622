"""
Урок 34 - Датаклассы в Python

Датаклассы в Python специальные классы которые являются своим своего рода синтаксическим сахаром Они упрощают создание обычных классов и избавляют нас от необходимости писать некоторые вещи Например они автоматически создают инициализатор а также автоматически описывают некоторые специальные методы
"""

from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    last_name: str
    age: int
    hobbies: list = field(default_factory=list)

    def __str__(self)->str:
        """
        Строковое представление объекта сделано для красивой печати экземпляров класса в вашем коде, чтобы это радовало ваш глаз. Когда НЕТ str - работает автоматичски repr
        """
        return f"Сотрудник: {self.name} {self.last_name}. Возраст: {self.age}\nХобби: {', '.join(self.hobbies)}"

    def __repr__(self)-> str:
        return f"Employee(name='{self.name}', last_name='{self.last_name}', age={self.age} )"


emp_1 = Employee("Иван", "Сергеев", 22, ["Пиво", "Хоккей", "Девушки"])
emp_2 = Employee("Мария", "Петрова", 24, ["Йога","Котики","Розовые свитера"])
print(emp_1)
print(emp_2)
# ValueError: mutable default <class 'list'> for field hobbies is not allowed: use default_factory