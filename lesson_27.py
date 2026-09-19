"""
Lesson 27 - Знакомство с ООП
"""


class Fridge:
    # Атрибуты класса
    model = "Бирюса 26 Pro Max"
    year = 2026

    def __init__(self, color: str, serial_number: str):
        self.color = color
        self.serial_number = serial_number
        self.products: list = []

    def __str__(self):
        result_str = f'Модель: "{self.model}\nГод выпуска:{self.year}\nСерийный номер: {self.serial_number}\nКол-во продуктов: {len(self.products)}"'
        return result_str

    def add_product(self, new_product: str) -> None:
        if isinstance(new_product, str):
            self.products.append(new_product)
        else:
            raise ValueError("В холодильник можно ложить только строки!")

    def is_product(self,  check_product: str) -> bool:
        return check_product.lower() in [product.lower() for product in self.products]



my_fridge = Fridge("чёрный", "0001")
my_father_fridge = Fridge("белый", "0002")


my_fridge.products.append("Молоко") # Так мы больше не делаем
my_fridge.add_product("Айран")

print(my_fridge.is_product("АЙРАН"))
print(my_fridge.is_product("МоЛоКО"))

print(my_fridge)
print(my_father_fridge)
