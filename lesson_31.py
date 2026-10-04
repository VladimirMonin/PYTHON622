"""
Lesson 31
Наследование классов в Python

Наследование в Python решает проблему дублирования кода. Вы можете создать класс-родитель, описать в нем 80% логики, общей для всего семейства ваших классов, и сделать несколько классов-наследников, которые полностью наследуют всю логику этого родителя.

При этом есть смысл делать наследование только в том случае, когда ваш наследник отличается от родителя хоть чем-нибудь.
"""


class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Двигатель {self.brand} {self.model} {self.year} запущен. Врум-врум!")

    def stop_engine(self):
        print(f"Двигатель {self.brand} {self.model} {self.year} остановлен.")

    def honk(self):
        print(f"{self.brand} {self.model} сигналит: Бип-бип!")


class LadaBlackBerry(Car):
    def __init__(self, brand: str, model: str, year: int, lighting: str = "LED"):
        super().__init__(brand, model, year)  # Вызов конструктора родителя
        self.lighting = lighting  # Добавляем новое свойство для наследника

    def fly(self):
        print(f"{self.brand} {self.model} {self.year} полетела в Хогвартс! 🚀")

    def honk(self):
        # Расширяем! Сначала вызываем родительский метод, а потом добавляем свою логику
        super().honk()  # Вызов метода родителя
        print(f"Пафосно сигналит {self.brand} {self.model}!")


lada = LadaBlackBerry("Lada", "BlackBerry", 2023)
lada.start_engine()
lada.fly()
lada.honk()
