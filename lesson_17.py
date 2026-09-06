"""
Урок 17
- двойная декорация функций
- декоратор с параметрами
- генарторы
- разница между генератором и списком
- функции генераторы
- yield
- Аннотация генераторов
- send и return в генераторах
- Функцию генератор для генератора пословиц
"""


def decorator_1(func):
    def wrapper(*args, **kwargs):
        print("Внешняя обвертка для конфетки")
        result = func(*args, **kwargs)
        print("Внешняя обвертка для конфетки - развернули")
        return result

    return wrapper


def decorator_2(func):
    def wrapper(*args, **kwargs):
        print("Внутренняя обвертка для конфетки")
        result = func(*args, **kwargs)
        print("Внутренняя обвертка для конфетки - развернули")
        return result

    return wrapper


@decorator_1
@decorator_2
def candy_foo(message: str) -> str:
    return f"Привет из candy_foo {message}!"


print(candy_foo("Ом-ном-ном. Съели конфетку!"))


def letters_check_decorator(letter: str = "р", count: int = 1):
    def decorator(func):
        def wrapper(*args):
            print(f"Проверяем наличие буквы '{letter}' в слове {args[0]}")
            if args[0].lower().count(letter) >= count:
                raise ValueError(
                    f"Слово {args[0]} содержит букву '{letter}' {count} раз(а)"
                )

            else:
                result = func(*args)
                return result

        return wrapper

    return decorator


@letters_check_decorator(letter="я", count=1)
def get_hello_message(name: str) -> str:
    return f"Привет, {name}!"


print(get_hello_message("Михаил"))
print(get_hello_message("Пётр"))


########

print(range(1, 10))
print(type(range(1, 10)))
print(list(range(1, 10)))

# for i in range(1, 10):
#     print(i)

my_range = range(1, 10)
# print(next(my_range)) # это не будет работать

my_generator = (i for i in range(1, 3))
print(next(my_generator))
print(next(my_generator))
# print(next(my_generator))# StopIteration error

print("Цикл по генератору")
for i in my_generator:
    print(i)


def my_generator_func():
    for i in range(1, 3):
        yield i


for i in my_generator_func():
    print(i)


# my_super_big_range = list(range(1, 1_000_000_000_000)) # MemoryError - мы не можем это создать.

# my_super_big_list = [i**3 for i in range(1, 1_000_000_000)]

# my_super_big_generator = (i**3 for i in range(1, 1_000_000_000))

# for i in my_super_big_generator:
#     print(i)


proverbs = [
    "Ум хорошо, а два лучше.",
    "Ум — горячая штука.",
    "Ум всё голова.",
    "Умом Россию не понять.",
    "Ум бережет, а глупость губит.",
    "Ум в голову приходит.",
    "Ум от ума не горит.",
    "Умом нагружен, а волосы развеваются.",
    "Умом обдумал, а ногами пошел.",
    "Ум — сокровище, не пропадет без него и копье на ветру.",
    "Ум — грех, а бес — мера.",
    "Ум есть богатство.",
    "Ум роднит народы.",
    "Ум краток, да забот — бездна.",
    "Ум не камень, взял и положил.",
    "Ум не велит, а наставляет.",
    "Ум с мерой, а глупость без меры.",
    "Ум — сокол, глаз его — телескоп.",
    "Ум — не конская морда, не разобьешь.",
    "Ум — семь пядей во лбу.",
    "Ум — не барсук, в нору не залезет.",
    "Ум в голове, а не на ветру.",
    "Ум греет душу, а глупость терпение.",
    "Ум служит человеку, а глупость — хозяином.",
    "Ум мил, да безумству хозяин.",
    "Ум в труде, да наслаждение в праздности.",
    "Ум глаза исправляет.",
    "Ум человека не обманешь.",
    "Ум на подобии огня — без сна не останешься.",
    "Ум к уму приходит.",
    "Ум с пользой тратит время.",
    "Ум желание творит.",
    "Ум общего дела дело.",
    "Ум — друг, а воля — враг.",
    "Ум — бесценное сокровище.",
    "Ум тонок, да разум невелик.",
    "Ум — враг бедности.",
    "Ум — теремок, да не на прокол.",
    "Ум силен, да не камень.",
    "Ум рассудит, что сердце не посоветует.",
    "Ум — подкова, а топор — ось.",
    "Ум легче камня, да весомей золота.",
    "Ум не вешать на гроздья.",
    "Ум — не мешок, на плечи не вешай.",
    "Ум — лучшая победа.",
    "Ум — в суде велик, а в деле своем мал.",
    "Ум голове краса.",
    "Ум — сокровище, а глупость — нищета.",
    "Ум человека — огонь, а глаза — масло.",
    "Ум — путь, а дорога — конец.",
    "Ум стоит денег.",
    "Ум от смеха бьет в ладоши.",
    "Ум — коза, к барскому плечу привыкает.",
    "Ум — лезвие, а лень — ржавчина.",
    "Ум на вершине — мир в руках.",
]

variants = [
    "кот",
    "шеф",
    "мозг",
    "лес",
    "сяоми",
    "код",
    "рот",
    "мёд",
    "дота",
    "год",
    "час",
    "друг",
    "жена",
    "муж",
    "айфон",
    "работа",
]

from random import choice
from typing import Generator

def proverbs_generator(proverbs_list: list[str], variants_list: list[str]) -> Generator[str]:
    # Переменная под результат
    ready_proverbs: set[str] = set()

    # Доступный максимум
    max_proverbs = len(proverbs_list) * len(variants_list)

    # Генерация пословиц
    while len(ready_proverbs) < max_proverbs:
        proverb = choice(proverbs_list)
        variant = choice(variants_list)
        new_proverb = proverb.replace("Ум", variant)

        if new_proverb not in ready_proverbs:
            ready_proverbs.add(new_proverb)
            yield new_proverb


user_input = int(input("Сколько вы хотите пословиц?"))

for _ in range(user_input):
    print(next(proverbs_generator(proverbs, variants)))

# Альтернативный вариант запуска

count = 0
while count < user_input:
    print(next(proverbs_generator(proverbs, variants)))
    count += 1

"""В Python для аннотации генераторов используется класс Generator из модуля typing. Этот тип данных является универсальным (generic) и принимает три параметра: тип возвращаемых значений (yield), тип значений, которые могут быть отправлены в генератор через метод send (send), и тип значения, которое генератор возвращает при завершении через оператор return (return).

Если вы создаете простой генератор, который только выдает значения и не принимает ничего извне, его часто аннотируют как Iterable или Iterator. Однако использование Generator[YieldType, None, None] является более точным и полным способом описания поведения функции-генератора, особенно в сложных сценариях асинхронного программирования или при реализации протоколов взаимодействия.

Generator [one, two, three]
- One - тип возвращаемых значений (yield)
- Two - тип значений, которые могут быть отправлены в генератор через метод send (send)
- Three - тип значения, которое генератор возвращает при завершении через оператор return (return)

В современных версиях Python, начиная с 3.9, можно использовать встроенные коллекции для аннотаций, но для Generator все еще требуется импорт из typing или collections.abc. Правильное указание типов помогает статическим анализаторам кода, таким как MyPy, выявлять ошибки несовместимости типов на этапе разработки, что значительно повышает надежность и читаемость кодовой базы проекта.

Для асинхронных генераторов в языке предусмотрен отдельный тип AsyncGenerator. Он принимает только два параметра: тип генерируемых значений и тип значений, отправляемых в генератор. Это связано с тем, что асинхронные генераторы в Python не поддерживают возвращение финального значения через return так, как это делают обычные генераторы, поэтому третий параметр в их аннотации отсутствует."""


def test_generator() -> Generator[str, str, str]:
    data = ["Первое слово", "Второе слово", "Третье слово"]
    for item in data:
        received = yield item
        print(f"Получено: {received}")

        if received is not None:
            yield f"{item} - обработано с {received}"

    return "Генератор завершен"


result = test_generator()
print(next(result))  # Получаем первое значение

print(
    result.send("данные для обработки")
)  # Отправляем данные и получаем обработанное значение
print(next(result))  # Генератор завершен
print(next(result))
print(next(result))