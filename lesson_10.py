# Урок 10
"""
Закрываем тему словарей и переходим к функциям
Объявление функции
Типы аргументов функции
Аннотации типов входных и выходных данных (пока без Typing)
"""

# uv add tabulate
# uv add openai
# from tabulate import tabulate
# from random import choice
# from openai import OpenAI

# config = {
#     "base_url": "https://polza.ai/api/v1",
#     "api_key": "pza_zNqusy0o4Q6kmAtBqqtoCt2V2qtLnN2j",
#     "model": "google/gemma-4-31b-it",
#     "image": False,
# }

# """
# keys
# values
# items
# """
# MODEL = config["model"]
# BASE_URL = config["base_url"]
# API_KEY = config["api_key"]
# IMAGE_SUPPORT = config["image"]

# PROMPT = "Расскажи смешной анкдот про обезьянку и {theme}"
# THEMES = ["Гитхаб", "ИИ агентов", "Бекенд разработку", "Веб-разработку", "Девопсов"]

# random_theme = choice(THEMES)
# final_promt = PROMPT.format(theme=random_theme)
# print("Запрос будет вот таким: ", final_promt)


# client = OpenAI(
#     base_url=BASE_URL,
#     api_key=API_KEY,
# )

# completion = client.chat.completions.create(
#     model=MODEL, messages=[{"role": "user", "content": final_promt}]
# )

# # print(completion.choices[0].message.content)
# # print("Токены генерации", completion.usage.completion_tokens)
# # print("Токены промпта", completion.usage.prompt_tokens)
# # print("Токенов всего", completion.usage.total_tokens)
# # print("Цена генерации", completion.usage.cost_rub)

# # Пакуем в словарь и выводим табулейт результат генерации

# result_data = {
#     "completion_tokens": completion.usage.completion_tokens,
#     "prompt_tokens": completion.usage.prompt_tokens,
#     "total_tokens": completion.usage.total_tokens,
#     "cost_rub": completion.usage.cost_rub,
# }

# # Выводим таблицу из словаря
# print(tabulate(result_data.items(), headers=["Тип данных", "Значение"], tablefmt="grid"))


##########################################

"""Функции в Python объявляются через ключевое слово `def`, что означает сокращение от *define*, то есть «определение». Называются они с использованием глагола, также могут присутствовать прилагательное и существительное.

Правила нейминга остаются теми же, что и для переменных в Python: нижний регистр, пробелы запрещены, вместо них должны использоваться нижние подчеркивания; никаких спецсимволов, название не может начинаться с цифры.

На английском языке, в отличие от переменных, здесь мы можем и должны использовать глагол. Название функции должно быть максимально понятным, по нему должно быть ясно, что она делает.

Если она читает конфиг — значит, «читает». Если она добывает его откуда-то из интернета — используем соответствующий глагол."""

# def hello_world():
#     print("Hello World!")

# hello_world()
# result = hello_world()

# def get_hello_string(name):
#     return f"Привет, {name}"

# hello_string = get_hello_string("Иван")
# print(hello_string)

"""
Позиционные аргументы так называются, потому что внутрь функции они попадают согласно позиции при передаче. Таким образом, если мы сделаем функцию `getHelloString`, которая будет содержать два параметра, `firstName` и `lastName`, печатать эти вещи функция будет согласно порядку передачи аргументов.

Также существуют еще так называемые keyword-аргументы. Их можно передать в любом порядке, потому что вы буквально говорите, что куда поместить.
"""

# def print_hello_string(first_name, last_name):
#     print(f"Привет, Имя:{first_name}, Фамилия:{last_name}")

# print_hello_string("Филлип", "Киркоров")
# print_hello_string("Киркоров", "Филлип")
# print_hello_string(last_name="Киркоров", first_name="Филлип")

def print_hello_string2(first_name, last_name, age):
    print(f"Привет, Имя:{first_name}, Фамилия:{last_name} Возраст:{age}")

print_hello_string2("Михаил", "Галустян", age=30)

#
print_hello_string2(age=30, "Михаил", "Галустян")
# Код ниже не будет работать, потому что мы хоть и можем передавать смешанные типы аргументов внутрь функции, они должны идти в определенном порядке, а именно: сначала позиционные аргументы, потом keyword-аргументы.

str - строка
int - число
float - дробное число
list - список
dict - словарь
set - множество
tuple - кортеж
list[str]- список строк
list[int|float] - список чисел или дробных
dict[str, float|int] - словарь где ключи строки, а значения числа или дробные числа

"""
Выше представлены базовые аннотации типов в Python. Обычно их указывают для функций: для аргументов, которые идут на вход в функцию, и для типов данных, которые выходят из функции.

Есть специализированные инструменты типа MyPy, предназначенные для проверки этих значений, а также для поиска логических ошибок. Пайплайн обозначает логическое «или»: вы можете указать несколько типов данных. Но, как правило, большое количество типов данных не указывается, потому что если ваша функция может принимать строки, числа или кортежи, наверное, стоит задуматься о логике, так как внутри эти вещи будут совершенно по-разному обрабатываться.

Первая строка функции, где указаны название функции, аргументы, типы входных аргументов и типы исходящего значения из функции, называется сигнатурой. И, как правило, по хорошей сигнатуре можно сказать, чем именно занимается функция, не читая ни её код, ни саму документацию.
"""

# def sum_numbers(a: int, b:int)-> int:
#     """
#     :param a: Первое число
#     :param b: Второе число
#     :return: Сумма двух чисел a и b
#     """
#     return a + b

# # a = input("Введите число а")
# # b = input("Введите число b")

# numbers = [10, 10]


# print(sum_numbers(numbers[0], numbers[1]))

# def print_names(names: list[str]):
#     [print(name) for name in names]

# names = ["Боб", "Алиса"]

# print_names(names)


# uv add tabulate
# uv add openai
from tabulate import tabulate
from random import choice
from openai import OpenAI

config = {
    "base_url": "https://polza.ai/api/v1",
    "api_key": "YOUR_API_KEY",
    "model": "google/gemma-4-31b-it",
    "image": False,
}

"""
keys
values
items
"""
from openai import OpenAI


MODEL = config["model"]
BASE_URL = config["base_url"]
API_KEY = config["api_key"]
IMAGE_SUPPORT = config["image"]

PROMPT = "Расскажи смешной анкдот про обезьянку и {theme}"
THEMES = ["Гитхаб", "ИИ агентов", "Бекенд разработку", "Веб-разработку", "Девопсов"]

random_theme = choice(THEMES)
final_promt = PROMPT.format(theme=random_theme)
print("Запрос будет вот таким: ", final_promt)


# client = OpenAI(
#     base_url=BASE_URL,
#     api_key=API_KEY,
# )


# completion = client.chat.completions.create(
#     model=MODEL, messages=[{"role": "user", "content": final_promt}]
# )

# print(completion.choices[0].message.content)
# # print("Токены генерации", completion.usage.completion_tokens)
# # print("Токены промпта", completion.usage.prompt_tokens)
# # print("Токенов всего", completion.usage.total_tokens)
# # print("Цена генерации", completion.usage.cost_rub)

# # Пакуем в словарь и выводим табулейт результат генерации

# result_data = {
#     "completion_tokens": completion.usage.completion_tokens,
#     "prompt_tokens": completion.usage.prompt_tokens,
#     "total_tokens": completion.usage.total_tokens,
#     "cost_rub": completion.usage.cost_rub,
# }

# # Выводим таблицу из словаря
# print(
#     tabulate(result_data.items(), headers=["Тип данных", "Значение"], tablefmt="grid")
# )


def get_openai_client(base_url: str, api_key_str) -> OpenAI:
    return OpenAI(base_url=base_url, api_key=api_key_str)


def request_openai(client: OpenAI, messages: list[dict], model: str) -> dict:
    completion = client.chat.completions.create(
        model=MODEL, messages=[{"role": "user", "content": final_promt}]
    )

    text_response = completion.choices[0].message.content

    messages.append({"role": "assistant", "content": text_response})

    response_dict = {
        "messages": messages,
        "completion_tokens": completion.usage.completion_tokens,
        "prompt_tokens": completion.usage.prompt_tokens,
        "total_tokens": completion.usage.total_tokens,
        "cost_rub": completion.usage.cost_rub,
    }
    return response_dict

def print_stats_response(response_dict: dict) -> None:
    response_dict.pop("messages")
    print(tabulate(response_dict.items(), headers=["Тип данных", "Значение"], tablefmt="grid"))


def main():
    client = get_openai_client(BASE_URL, API_KEY)
    messages = [{"role": "user", "content": final_promt}]
    response_dict = request_openai(client, messages, MODEL)
    print_stats_response(response_dict)
    print(response_dict["messages"][-1])

main()