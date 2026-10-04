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

    def __init__(self, political_name):
        self.political_name = political_name

class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Игрушка: {self.name}, Цена: {self.price} руб."


class BushMetalMattrToy(Toy, MetallToyMixin, PoliticalDesignMixin):
    def __init__(self, name, price, political_name):
        Toy.__init__(self, name, price)
        PoliticalDesignMixin.__init__(self, political_name)

    def get_info(self):
        return f"Игрушка: {self.name}, Цена: {self.price} руб., Политический дизайн: {self.political_name}, Материал: {self.material}"