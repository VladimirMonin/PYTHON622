"""
Урок 32. Наследование
"""


class Bird:
    def __init__(self, name):
        self.name = name
        self.wings = 2

    def fly(self):
        return f"{self.name} летит в небе!"

    def sing(self):
        return f"{self.name} поет свою песню!"

    def special_skill(self):
        return f"{self.name} закладывает бочку в воздухе!"


class Goose(Bird):
    def __init__(self, name: str, owner: str):
        super().__init__(name)
        # self.name = name
        self.owner = owner

    def special_skill(self):
        return f"{self.name} гоняет детей по ферме!"

    def sing(self):
        # Аналог super().sing()
        # return self.__class__.__bases__[0].sing(self)
        # return Bird.sing(self)

        result = super().sing()  # Вызов метода родителя
        return result + "га-га-га!"  # Добавляем свою логику


goose = Goose("Пыжик", "Фёдор")
print(goose.special_skill())
print(goose.sing())
