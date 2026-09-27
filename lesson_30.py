"""
Специальные методы в Python — это те методы, которые Python использует в специальных случаях. Например, при создании экземпляра класса, при попытке привести экземпляр класса к строковому или к булевому значению, при попытке получить длину экземпляра класса, при сравнении разных экземпляров на больше и меньше или при попытке сделать математическую операцию между экземплярами класса. И даже в тех случаях, когда вы пытаетесь экземпляр класса «запустить», получается, что специальные методы описывают поведение класса в кодовой среде.

__init__ - запускается при инициализации эклемпляра
__str__ - при принте или при приведении через str()
__len__ - при помещении в строенную функцию длины
__bool__ - при if или при приведении через bool()
__call__ - делает экземпляр класса вызываемым - может принимать аргументы

-------
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RobotToy:
    MINIMAL_BATTERY_LEVEL = 20

    def __init__(self, name: str, size: int, battery_level: int):
        # Запускается на создании экземпляра
        self.name = name
        self.size = size
        self.battery_level = battery_level
        logger.debug(self.__str__())

    def __str__(self) -> str:
        return f"Экземпляр {self.__class__.__name__} создан\nИмя: {self.name}\nРазмер: {self.size}.\nУровень заряда: {self.battery_level}"

    def __len__(self) -> int:
        return self.size

    def __bool__(self) -> bool:
        return self.battery_level > self.MINIMAL_BATTERY_LEVEL


robot_1 = RobotToy("ЖораТрон", 10, 80)
robot_2 = RobotToy("Оптимус", 5, 15)
robot_3 = RobotToy("Т1000", 15, 60)

robots = [robot_1, robot_2, robot_3]

print(robot_1)
print(robot_2)

print(len(robot_1))

if robot_1:
    print(f"{robot_1.name} заряжен")
else:
    print(f"{robot_1.name} разряжен")


if robot_2:
    print(f"{robot_2.name} заряжен")
else:
    print(f"{robot_2.name} разряжен")

robots.sort(key=len)
print(robots)
[print(robot) for robot in robots]