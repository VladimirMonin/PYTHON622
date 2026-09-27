"""
Специальные методы в Python — это те методы, которые Python использует в специальных случаях. Например, при создании экземпляра класса, при попытке привести экземпляр класса к строковому или к булевому значению, при попытке получить длину экземпляра класса, при сравнении разных экземпляров на больше и меньше или при попытке сделать математическую операцию между экземплярами класса. И даже в тех случаях, когда вы пытаетесь экземпляр класса «запустить», получается, что специальные методы описывают поведение класса в кодовой среде.

__init__ - запускается при инициализации эклемпляра
__str__ - при принте или при приведении через str()
__len__ - при помещении в строенную функцию длины
__bool__ - при if или при приведении через bool()
__call__ - делает экземпляр класса вызываемым - может принимать аргументы

-------

Ниже представлен перечень специальных методов Python для основных математических операций:

__add__(self, other)` — сложение (`+`);
__sub__(self, other)` — вычитание (`-`);
__mul__(self, other)` — умножение (`*`);
__truediv__(self, other)` — деление (`/`);
__iadd__(self, other)` — сложение с присваиванием (`+=`);
__isub__(self, other)` — вычитание с присваиванием (`-=`);
__imul__(self, other)` — умножение с присваиванием (`*=`);
__itruediv__(self, other)` — деление с присваиванием (`/=`).

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
        logger.debug("Был приведен к строке")
        return f"Экземпляр {self.__class__.__name__} создан\nИмя: {self.name}\nРазмер: {self.size}.\nУровень заряда: {self.battery_level}"

    def __len__(self) -> int:
        logger.debug("Была получена длина")
        return self.size

    def __bool__(self) -> bool:
        logger.debug("Был приведен к Bool")
        return self.battery_level > self.MINIMAL_BATTERY_LEVEL

    def __add__(self, other: RobotToy) -> RobotToy:
        logger.debug("Была попытка объединить двух роботов")
        if not isinstance(other, RobotToy):
            logger.error(f"Была попытка скрестить робота с {type(other)}")
            raise ValueError(f"Поддерживаются операции сложения только с {self.__class__.__name__}")
        
        new_name = f"{self.name}-{other.name}"
        new_size = self.size + other.size
        new_battary_level = max([self.battery_level, other.battery_level])
        new_robot = RobotToy(new_name, new_size, new_battary_level)

        return new_robot


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

"""
Чем отличаются операции `a + b` и `a += 2`? В случае обычного плюса у нас создается новый экземпляр числа.

В случае `a += 2` у нас видоизменяется число `a`. Такая операция называется in-place, то есть «на месте».

Это означает, что происходит изменение текущего экземпляра класса, с которым мы работаем. В данном случае это экземпляр класса, на который ссылается переменная `a`.

А вот в случае `a + b` у нас рождается третий объект — экземпляр класса, и он будет являться новым объектом.
"""
a = 2
b = 2
c = a + b
a += 2

robot_4 = robot_1 + robot_2 + robot_3
print(robot_4)

robot_1 += robot_2
print(robot_1)

# robot_1 + "Человек" # ValueError: Поддерживаются операции сложения только с RobotToy