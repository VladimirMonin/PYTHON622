a = 15

print(a)


def foo():
    print(a)


def foo1(a):
    print(a)


def foo2(a):
    print(a)


foo1(1)
foo1(2)

from typing import Callable


def counter(start: int = 0) -> Callable:
    # Тут хранится start
    current = start

    def inner() -> int:
        nonlocal current
        current += 1
        return current

    return inner


c1 = counter(5)
print(c1())
print(c1())

"""
Callabe[[int, int], float]
Callable[[ТипВызова1, ТипВызова2], ТипВозврата]

В Python аннотация `Callable` из модуля `typing` (или встроенная в современных версиях) используется для обозначения объектов, которые можно вызвать как функции.


Если количество аргументов не важно - можно исползьовать ...
Или просто оставить Callable
"""


def simple_decorator(foo: Callable) -> Callable:
    def wrapper():
        print("До вызова функции")
        foo()
        print("После вызова функции")

    return wrapper


def print_foo():
    print("Привет из функции!")


decorated_print_foo = simple_decorator(print_foo)
decorated_print_foo()


@simple_decorator
def print_foo1():
    print("Привет из функции!")


print_foo1()


def simple_decorator_2(foo: Callable) -> Callable:
    def wrapper(arg):
        print(f"До вызова функции с аргументом {arg}")
        result = foo(arg)
        print(f"После вызова функции с аргументом {arg}")
        return result

    return wrapper


def print_foo2(message: str) -> str:
    return f"Привет из print_foo2 {message}!"


# 1. Сначала создаете переменную decorated_print_foo_1
# 2. Потом запускаете ее и результат работы вам нужно положить в переменную.

decorated_print_foo_2 = simple_decorator_2(print_foo2)

result_1 = decorated_print_foo_2("Сообщение 1")
result_2 = decorated_print_foo_2("Сообщение 2")

print(result_1, result_2)


def simple_decorator_3(foo: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"До вызова функции с аргументом")
        result = foo(*args, **kwargs)
        print(f"После вызова функции с аргументом")
        return result

    return wrapper


@simple_decorator_3
def print_hello_by_name(name: str) -> None:
    print(f"Привет {name}!")


@simple_decorator_3
def print_hello_by_full_name(first_name: str, last_name: str) -> None:
    print(f"Привет, уважаемый(ая) {last_name}, {first_name}")


print_hello_by_name("Антон")
print_hello_by_full_name("Антон", "Иванов")


from typing import Any, Callable
from time import perf_counter, sleep

# Засекаем время старта
start_time = perf_counter()

# Спим 5 секунд
# sleep(5)

# Засекаем время финиша
finish_time = perf_counter()

# Считаем разницу было - стало
duration = finish_time - start_time

print("Время выполнения: ", duration)

# Округление до 3 знаков после запяток
print(round(duration, 3))
print(f"{duration:.3f}")


def perf_timer_decorator(foo: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = perf_counter()
        result = foo(*args, **kwargs)
        finish_time = perf_counter()
        duration = finish_time - start_time
        print(f"Время выполнения {foo.__name__}: {duration:.6f} секунд")
        return result

    return wrapper


from cities import cities_list
from pprint import pprint


@perf_timer_decorator
def city_sorter(city_collection: list[dict], sort_keys: list[str]) -> list[dict]:
    sorted_citis = list(
        sorted(city_collection, key=lambda city: [city[key] for key in sort_keys])
    )

    return sorted_citis


sort_keys = ["district", "population"]

result = city_sorter(cities_list, sort_keys)


# pprint(result[100:])

POLZA_API_KEY = "YOUR_API_KEY"
BASE_URL_POLZA = "https://polza.ai/api/v1"
MODEL = "google/gemini-3.5-flash-lite"

# uv init
# uv add openai
from openai import OpenAI

@perf_timer_decorator
def text_request_polza_ai(
    message: str,
    model: str = MODEL,
    base_url: str = BASE_URL_POLZA,
    api_key: str = POLZA_API_KEY,
) -> str:
    client = OpenAI(base_url=base_url, api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
    )

    result = completion.choices[0].message.content
    return result


print(text_request_polza_ai("Расскажи анекдот про программиста"))



def perf_timer_decorator2(round_param: int = 3) -> Callable:
    def decorator(foo: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            start_time = perf_counter()
            result = foo(*args, **kwargs)
            finish_time = perf_counter()
            duration = finish_time - start_time
            rounded_duration = round(duration, round_param)
            print("Время работы", rounded_duration)
            return result

        return wrapper

    return decorator

        
@perf_timer_decorator2(round_param=5)
def foo_sleep():
    sleep(5)
    print("Поспал")