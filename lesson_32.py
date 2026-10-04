"""
Урок 32. Наследование
"""
 

class WoodenToyMixin:
    material = "Дерево"

    def get_info(self):
        return f"Инфа из класса WoodenToy: {self.name}"

class MetallToyMixin:
    material = "Металл"

    def get_info(self):
        return f"Инфа из класса MetallToy: {self.name}"

class PoliticalDesignMixin:
    type_design = "Политический дизайн"

    def __init__(self, **kwargs):
        self.political_name = kwargs.get("political_name")

class Toy:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.price = kwargs.get("price")
        super().__init__(**kwargs)
    def get_info(self):
        return f"Игрушка: {self.name}, Цена: {self.price} руб."


class BushMetalMattrToy(Toy, MetallToyMixin, PoliticalDesignMixin):
    def __init__(self, name, price, political_name):
        super().__init__(name=name, price=price, political_name=political_name)

    def get_info(self):
        return f"Игрушка: {self.name}, Цена: {self.price} руб., Политический дизайн: {self.political_name}, Материал: {self.material}"


bush_metal_toy = BushMetalMattrToy(name="Буш", price=1000, political_name="Политический Буш")
print(bush_metal_toy.get_info())