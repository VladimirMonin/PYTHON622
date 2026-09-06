"""
# Lesson 15
- Области видимости
- Замыкания
"""

"""
Области видимости в пайтон:
- Built in - встроенная. Олимп. Там живут print, len и другие встроенные в Python инструменты
- Global - ваш файл
- Local - облатсь видимости внутри функции
- Nonlocal - не то, чтобы область видимости, но используется когда функция вложена в другую функцию
"""


a = 15

def foo1():
    a = 5
    print(f"Локлаьно foo1 {a=}")

def foo2():
    global a
    a = 5
    print(f"Локлаьно foo2 {a=}")

print("Глобально ДО функции foo1", a)
foo1()
print("Глобально ПОСЛЕ функции foo1", a)
foo2()
print("Глобально ПОСЛЕ функции foo2", a)


"""
Важно отметить то, что Python ищет имена, когда они требуются, начиная с текущей области видимости и выше. Например, в функции номер 3 Python попытается, когда будет необходимо распечатать, сделать `print(name)`. Он попытается найти переменную `name` в текущей области видимости.

Для него текущая область видимости будет локальной областью видимости этой функции. И если она там определена, он ее использует. Если же переменная не будет определена внутри функции, он просто пойдет выше и найдет ее (в нашем случае — в глобальной области видимости).

И распечатает уже другое имя. Поэтому, в зависимости от того, определена ли переменная в функции номер 3 или нет, мы сможем получить разные результаты при вызове этой функции.

При этом стоит также обратить внимание, что имя самой функции `print` Python найдет еще выше — во встроенной области видимости, там, где хранятся технические служебные имена встроенных в Python функций.

Поэтому она называется built-in, то есть «встроенная».
"""


name = "Валентин"

def foo3():
    name = "Алина"
    print(name)

foo3()

from typing import Callable
banana = print
banana("Банановый принт")



title = "Колобок"

def foo4():
    # Локальная область
    title = "Властелин Колец"
    print("Локально foo4", title)
    
    def inner_foo4():
        title = "Месть Чакки 4"
        print("Иннер foo4", title)

    inner_foo4()

foo4()

###############
def foo5():
    # Локальная область
    title = "Властелин Колец"
    print("Локально foo5", title)
    
    def inner_foo5():
        # NONLOCAL возможность выходить наружу во внешнюю функцию
        nonlocal title
        title = "Месть Чакки 5"
        print("Иннер foo5", title)

    inner_foo5()
    print("Локально foo5 после inner_foo5", title)

foo5()


def counter(start: int = 0) -> Callable:
    # start является локальным именем counter
    def inner() -> int:
        nonlocal start
        start += 1
        return start
    
    return inner

с1 = counter()
c2 = counter(5)

print(с1())
print(c2())

print(с1())
print(c2())


######################### ФУНКЦИЯ НОРМАЛИЗАТОР ХЕШТЕГОВ С КЕШИРОВАНИЕМ
from typing import Iterable

def normilize_tags() -> Callable:
    current_collection = None
    last_raw_collection = None

    def inner(tag_collection: Iterable[str]) -> list[str]:
        nonlocal last_raw_collection, current_collection
        if last_raw_collection == tag_collection:
            return current_collection

        else:
            current_collection = ["#" + tag.strip().lower().replace(" ", "_") for tag in tag_collection]
            last_raw_collection = tag_collection
            return current_collection
    
    return inner


normalizer_tags = normilize_tags()

tags = ["Купил компьютер", "поКушал", " Котик СпИТ"]

result = normalizer_tags(tags)
print(result)
result2 = normalizer_tags(tags)
print(result2)