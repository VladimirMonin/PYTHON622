"""
Lesson 24 - Логирование в Пайтон
"""

"""
в стандартном модуле logging есть четыре основные сущности — Logger, Handler, Formatter и Filter. Они работают вместе, но не все буквально находятся «внутри» логгера.
"""

import logging
from utils_24.polza_utils import request_api

logging.basicConfig(
    level=logging.DEBUG,  # Что будет логироваться. DEBUG - все сообщения, INFO - только информационные и выше, WARNING - предупреждения и выше, ERROR - ошибки и выше, CRITICAL - только критические ошибки
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",  # Как вообще лог строка форматируется
    datefmt="%Y-%m-%d %H:%M:%S",  # Как форматируется дата
    handlers=[
        logging.StreamHandler(),  # вывод в консоль
        logging.FileHandler(
            "lesson_24.log", mode="a", encoding="utf-8"
        ),  # вывод в файл
    ],
)

if __name__ == "__main__":
    logging.debug("Приложение запущено")
    prompt = "Рецепт тех самых пирожков!"
    response = request_api(prompt)
    logging.debug("Приложение завершило работу")
