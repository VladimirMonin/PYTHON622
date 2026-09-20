"""
Lesson 28

Итак, сегодня мы познакомимся с концепциями метода экземпляра, метода класса, static method и еще раз поговорим про атрибуты экземпляра и атрибуты класса.
"""

class Fridge:
    server_soft_version: str = "0.0.1"
    server_url: str = "www.birusa.ru/api/v1/"
    avalible_models: list[str] = ["Бирюса", "Бирюса Плюс", "Бирюса Про", "Бирюса Про Макс"]

    def __init__(self, owner:str, model:str):
        self.owner = owner
        self. model = self.model_validator(model)
        self.current_soft_version = self.server_soft_version


    def __str__(self) -> str:
        return f"---\nВладелец: {self.owner}\nМодель:{self.model}\nТекущая прошивка: {self.current_soft_version}\n---"


    def model_validator(self, model: str):
        if model in self.avalible_models:
            return model

        else:
            raise ValueError(f"Недопустимое название модели! Допустимо: {self.avalible_models}")


    @classmethod
    def update_server_soft_version(cls, new_soft_version: str):
        cls.server_soft_version = new_soft_version

    def update_soft(self):
        if self.current_soft_version == self.server_soft_version:
            print(f"Нет нужды обновлятся текущая версия соответствует серверной {self.current_soft_version}")

        else:
            print(f"Прошивка обновилась c {self.current_soft_version} на {self.server_soft_version}")
            self.current_soft_version = self.server_soft_version

# fridge_1 = Fridge("Владимир", "Биюрса Про Макс Ультра Пультра Эдишн!") # ValueError: Недопустимое название модели! Допустимо: ['Бирюса', 'Бирюса Плюс', 'Бирюса Про', 'Бирюса Про Макс']
fridge_1 = Fridge("Владимир", "Бирюса Плюс")
fridge_2 = Fridge("Батя", "Бирюса Про Макс")

print(fridge_1)
print(fridge_2)

# fridge_1.update_server_soft_version("0.0.2")
Fridge.update_server_soft_version("0.0.2")

fridge_3 = Fridge("Брат", "Бирюса Про Макс")

###############################
print(fridge_1)
print(fridge_2)
print(fridge_3)

fridge_1.update_soft()

print(fridge_1)