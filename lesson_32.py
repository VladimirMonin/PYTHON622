"""
Урок 32. Наследование
"""

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} летит в небе!"

    def sing(self):
        return f"{self.name} поет свою песню!"

    def special_skill(self):
        return f"{self.name} закладывает бочку в воздухе!"


class Goose(Bird):
    def special_skill(self):
        return f"{self.name} гоняет детей по ферме!"

goose = Goose("Пыжик")
print(goose.special_skill())