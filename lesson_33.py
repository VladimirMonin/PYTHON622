"""
# Lesson 33 - Вспомить Миксины и разобраться с AbstractClass
"""
from abc import ABC, abstractmethod

class AbstractImage(ABC):
    def __init__(self, file_name: str):
        self.file_name = file_name

    def __str__(self) -> str:
        return f"Изображение: {self.file_name}\nТип: {self.__class__.__name__}"

    @abstractmethod
    def open(self):
        ...


class JpegImage(AbstractImage):

    def open(self):
        print(f"{self.file_name} открыт!")


class PngImage(AbstractImage):

    def open(self):
        print(f"{self.file_name} открыт!")


class AvifImage(AbstractImage):

    def open_file(self):
        print(f"{self.file_name} открыт!")

jpeg_1 = JpegImage("Котик.jpg")
jpeg_2 = JpegImage("Котик2.jpg")
png_1 = PngImage("Котик.png")
avif_1 = AvifImage("Котик.avif") # TypeError: Can't instantiate abstract class AvifImage without an implementation for abstract method 'open'

my_images_1 = [jpeg_1, jpeg_2, png_1]
my_images_2 = [png_1, avif_1]

for image in my_images_1:
    image.open()

print("Пошел второй цикл")

# Тут будет ошибка потому что у класса AvifImage НЕТ метода open
for image in my_images_2:
    image.open()