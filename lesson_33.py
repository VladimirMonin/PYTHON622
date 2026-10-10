"""
# Lesson 33 - Вспомить Миксины и разобраться с AbstractClass
"""

class JpegImage:
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name

    def open(self):
        print(f"{self.file_name} открыт!")


class PngImage:
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name

    def open(self):
        print(f"{self.file_name} открыт!")


class AvifImage:
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name

    def open_file(self):
        print(f"{self.file_name} открыт!")

jpeg_1 = JpegImage("Котик.jpg")
jpeg_2 = JpegImage("Котик2.jpg")
png_1 = PngImage("Котик.png")
avif_1 = AvifImage("Котик.avif")

my_images_1 = [jpeg_1, jpeg_2, png_1]
my_images_2 = [png_1, avif_1]

for image in my_images_1:
    image.open()

print("Пошел второй цикл")

# Тут будет ошибка потому что у класса AvifImage НЕТ метода open
for image in my_images_2:
    image.open()