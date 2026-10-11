"""
Урок 34 - Датаклассы в Python

Датаклассы в Python специальные классы которые являются своим своего рода синтаксическим сахаром Они упрощают создание обычных классов и избавляют нас от необходимости писать некоторые вещи Например они автоматически создают инициализатор а также автоматически описывают некоторые специальные методы
"""

from dataclasses import dataclass, field

class AgeValueError(ValueError):
    ...

@dataclass(order=True)
class Employee:
    name: str = field(compare=False)
    last_name: str = field(compare=False)
    age: int 
    hobbies: list = field(default_factory=list, compare=False)

    def __post_init__(self):
        self.__age_validator()

    def __str__(self)->str:
        """
        Строковое представление объекта сделано для красивой печати экземпляров класса в вашем коде, чтобы это радовало ваш глаз. Когда НЕТ str - работает автоматичски repr
        """
        return f"Сотрудник: {self.name} {self.last_name}. Возраст: {self.age}\nХобби: {', '.join(self.hobbies)}"

    def __repr__(self)-> str:
        return f"Employee(name='{self.name}', last_name='{self.last_name}', age={self.age} )"

    def __age_validator(self):
        if not isinstance(self.age, int):
            raise TypeError("Age должен быть числом")
        if not 0 < self.age < 120:
            raise AgeValueError("Возраст вне диапазона")
            
                
        

emp_0 = Employee("Дракула", "Граф", 666, ["Кровь", "Молодые девушки", "Пугать крестьян"])
emp_1 = Employee("Иван", "Сергеев", 22, ["Пиво", "Хоккей", "Девушки"])
emp_2 = Employee("Мария", "Петрова", 24, ["Йога","Котики","Розовые свитера"])
emp_3 = Employee("Глафира", "Беднякова", 35, ["Чтение литературы по саморазвитию","Богатый Папа Бедный папа","Квизы по Гарри Поттеру"])


my_employees = [emp_2, emp_1, emp_3]

my_employees.sort(reverse=True)
print(my_employees)

print(emp_1)
print(emp_2)
# ValueError: mutable default <class 'list'> for field hobbies is not allowed: use default_factory

print(emp_1 == emp_2) # Эта проверка работает
print(emp_1 != emp_2) # Эта проверка работает

# ЭТО ЗАРАБОТАЕТ ТОЛЬКО при включении параметра декоратора @dataclass(order=True)
print(emp_1 > emp_2)
print(emp_1 <= emp_2)