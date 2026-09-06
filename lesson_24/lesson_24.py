"""
Lesson 24 - Логирование в Пайтон
"""

"""
в стандартном модуле logging есть четыре основные сущности — Logger, Handler, Formatter и Filter. Они работают вместе, но не все буквально находятся «внутри» логгера.
"""

import logging
from utils_24.polza_utils import request_api
from logging.handlers import RotatingFileHandler
# uv add colorlog
from colorlog import ColoredFormatter


# Обработчик терминала
console_handler = logging.StreamHandler()

# Цветной форматтер для терминала
# Цветной форматтер
console_formatter = ColoredFormatter(
    fmt=(
        "%(asctime)s | %(log_color)s%(levelname)-8s%(reset)s | %(name)s | %(log_color)s%(message)s"
    ),
    datefmt="%H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_white,bg_red",
    },
)

console_handler.setFormatter(console_formatter)


logging.basicConfig(
    level=logging.DEBUG,  # Что будет логироваться. DEBUG - все сообщения, INFO - только информационные и выше, WARNING - предупреждения и выше, ERROR - ошибки и выше, CRITICAL - только критические ошибки
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",  # Как вообще лог строка форматируется
    datefmt="%Y-%m-%d %H:%M:%S",  # Как форматируется дата
    handlers=[
        console_handler,  # вывод в терминал
        RotatingFileHandler(
            "lesson_24.log", maxBytes=1024 * 1024 * 2, backupCount=3, encoding="utf-8"
        ),  # вывод в файл с ротацией
    ],
)

if __name__ == "__main__":
    logging.debug("Приложение запущено")
    prompt = "Рецепт тех самых пирожков!"
    response = request_api(prompt)
    logging.debug("Приложение завершило работу")

    # Остальные уровни логирования
    logging.warning("Это предупреждение")
    logging.error("Это ошибка")
    logging.critical("Это критическая ошибка")
