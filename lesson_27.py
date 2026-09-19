"""
Lesson 27 - Знакомство с ООП
"""


class Fridge:
    # Атрибуты класса
    model = "Бирюса 26 Pro Max"
    year = 2026

    def __init__(self, color: str, serial_number: int):
        self.color = color
        self.serial_number = serial_number
        self.products: list = []


my_fridge = Fridge("чёрный", 1)
my_father_fridge = Fridge("белый", 2)

my_fridge.products.append("колбаска")
my_father_fridge.products.append("коньяк")

print(my_fridge.products)
print(my_fridge.color)
print(my_fridge.model)

print(my_father_fridge.products)
print(my_father_fridge.color)
print(my_father_fridge.model)

