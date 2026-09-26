"""
Инкапсуляция в объектно-ориентированном программировании `Python` — это способ скрыть логику и информацию. Мы можем скрыть от внешнего мира — от других классов и от пользователей нашего класса — как атрибуты, так и методы собственного класса.

Делается это, как правило, для того, чтобы не сломать сложную внутреннюю логику. И здесь можно провести много параллелей: это как у пользователя автомобиля нет доступа к логике бортового компьютера напрямую, так и с биологией — было бы странно, если бы мы могли почесать свою печень или желудок или напрямую положить туда еду, сразу в желудок. Это было бы очень странно. Здесь и инженеры, и сама природа скрыли от нас реализацию внутренней логики и внутренней информации.
"""


class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        self.__max_speed_threshold: float = 500.0
        self.__max_speed: float = 250.0
        self.__vin_number: str = "BIN007"

    def __str__(self):
        return f"""
Информация по автомобилю
Модель: {self.model}
Цвет: {self.color}
Максимальная скорость: {self.__max_speed}
Серийный номер кузова: {self.__vin_number}
"""

    def get_max_speed(self) -> float:
        return self.__max_speed

    def __validate_max_speed(self, new_max_speed: float):
        if not isinstance(new_max_speed, float):
            raise ValueError("Новая скорость должна быть float")
        if new_max_speed > self.__max_speed_threshold:
            raise ValueError(
                f"Новая скорость должна быть ниже чем {self.__max_speed_threshold}"
            )

    def set_max_speed(self, new_max_speed: float) -> None:
        self.__validate_max_speed(new_max_speed)
        self.__max_speed = new_max_speed


car1 = Car("Деу Маркиз", "Красный")
print(car1.get_max_speed())

car1.set_max_speed(450.0)

print(car1.get_max_speed())

# car1.set_max_speed("Чебурек") # ValueError: Новая скорость должна быть float
# car1.set_max_speed(800.0) # ValueError: Новая скорость должна быть ниже чем 500.0

