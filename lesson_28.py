"""
Lesson 28

Итак, сегодня мы познакомимся с концепциями метода экземпляра, метода класса, static method и еще раз поговорим про атрибуты экземпляра и атрибуты класса.
"""

class Fridge:
    soft_version: str = "0.0.1"
    server_url: str = "www.birusa.ru/api/v1/"
    avalible_models: list[str] = ["Бирюса", "Бирюса Плюс", "Бирюса Про", "Бирюса Про Макс"]

    def __init__(self, owner:str, model:str):
        self.owner = owner
        self. model = self.model_validator(model)
        self.current_soft_version = self.soft_version


    def __str__(self) -> str:
        return f"---\nВладелец: {self.owner}\nМодель:{self.model}\nТекущая прошивка: {self.current_soft_version}\n---"


    def model_validator(self, model: str):
        if model in self.avalible_models:
            return model

        else:
            raise ValueError(f"Недопустимое название модели! Допустимо: {self.avalible_models}")

# fridge_1 = Fridge("Владимир", "Биюрса Про Макс Ультра Пультра Эдишн!") # ValueError: Недопустимое название модели! Допустимо: ['Бирюса', 'Бирюса Плюс', 'Бирюса Про', 'Бирюса Про Макс']
fridge_1 = Fridge("Владимир", "Бирюса Плюс")
fridge_2 = Fridge("Батя", "Бирюса Про Макс")

print(fridge_1)
print(fridge_2)