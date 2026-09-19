"""
Lesson 27 - Знакомство с ООП
"""

class TxtDocument:
    """
    Класс для работы с текстовыми документами. Каждый экземпляр привязан к конкретному файлу.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> list[str]:
        """
        Метод читает документ и возвращает список строк. Если документа нет?? автоматически обрабатывает переносы строк
        """
        with open(self.file_path, mode="r", encoding="utf-8") as file:
            list_strings = file.readlines()
            return [string.strip() for string in list_strings]

    def write(self, data: list[str]) -> None:
        """
        Берет список строк и перезаписывает документ автоматически обрабатывает переносы строк
        """
        with open(self.file_path, mode="w", encoding="utf-8") as file:
            prepeared_data = [string + "\n" for string in data]
            file.writelines(prepeared_data)

    def append(self, data: list[str]) -> None:
        """
        Дозаписывает в документ список строк автоматически обрабатывает переносы строк
        """
        with open(self.file_path, mode="a", encoding="utf-8") as file:
            prepeared_data = [string + "\n" for string in data]
            file.writelines(prepeared_data)


FILE_PATH = "lesson_27.txt"
txt_file = TxtDocument(FILE_PATH)

txt_file.write(["Привет, это первая строка", "А это вторая строка и перенос добавит метод!"])
txt_file.append(["Дозаписал третью строку. Метод тоже добавил пренос."])

print(txt_file.read())