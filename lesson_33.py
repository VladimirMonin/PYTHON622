# Lesson 33 - Вспомить Миксины!

class BaseBird:
    def __init__(self, name:str):
        self.name = name

    def voice(self)-> str:
        return f"{self.name} говорит: "

    def run(self):
        print(f"{self.name} неизвестно, может ли бегать?!")

    def fly(self):
            print(f"{self.name} неизвестно, может ли летать?!")

    def swim(self):
            print(f"{self.name} неизвестно, может ли плавать?!")


class RunMixin:
    def run(self):
        print(f"{self.name} бежит!")


class FlyMixin:
    def fly(self):
        print(f"{self.name} летит!")


class SwimMixin:
    def swim(self):
        print(f"{self.name} плывет!")

class RoboDuckV1(BaseBird, SwimMixin, FlyMixin):
     ...


class RoboDuckV2(SwimMixin, FlyMixin, BaseBird):
     ...

robo_duck_1 = RoboDuckV1("Скрудж")
robo_duck_2 = RoboDuckV2("Дональд")

robo_duck_1.fly()
robo_duck_2.fly()

# Сделаем MRO
print(RoboDuckV1.mro())
print(RoboDuckV2.mro())