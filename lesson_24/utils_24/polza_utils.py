import logging

logger = logging.getLogger(__name__)


def request_api(prompt: str) -> str:
    logger.info(f"Запрос к API с промптом: {prompt}")
    print("РАБОТАЕТ ФУНКЦИЯ!!!!")
    logger.info("Ответ от API получен")

    return "Ответ от API"
