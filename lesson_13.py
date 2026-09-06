# Lesson 13 - Lambda, функции высшего порядка, map, filter, sorted (?)

foo = lambda x, y: x + y

print(foo(10, 20))

names = ["БОБ", None, "ПИТЕР", "АЛИСА"]

banana = print
banana("Банан печатает!")

print(id(banana))
print(id(print))


def potato_machine(func, some_list: list):
    result = []
    for item in some_list:
        result.append(func(item))
    return result


def potato_cleaner(potato: str) -> str:
    return potato + "почищено"


potatos = [
    "картошка",
    "картошка",
    "картошка",
    "гнилая картошка",
    "картошка",
    "гнилая картошка",
    "картошка",
    "картошка",
]

cleaned_potatos = potato_machine(potato_cleaner, potatos)
print(cleaned_potatos)

################### Функция MAP
cleaned_potatos = list(map(potato_cleaner, potatos))
cleaned_potatos = list(map(lambda potato: potato + "почищено", potatos))

cleaned_potatos = [potato + "почищено" for potato in potatos]
cleaned_potatos = [f"{potato}почищено" for potato in potatos]

cleaned_potatos = []
for potato in potatos:
    cleaned_potatos.append(potato + "почищено")

# ################### Функция FILTER
"""
Если map всегда на выход отдаст столько сколько взял на вход
То фильтр может отдать меньше, или вообще пустую коллекцию.

Его особенность в том, что он принимает функцию, которая принимает один элекмент и возвращает
на выход True/False. Если True - элемент оставляется в коллекции, если False - удаляется из коллеции.

"""
potatos = [
    "картошка",
    "картошка",
    "картошка",
    "гнилая картошка",
    "картошка",
    "гнилая картошка",
    "картошка",
    "картошка",
]


# Функция высшего порядка для фильтрации
def potato_filter(func, potatos_list: list[str]) -> list:
    result = []

    for potato in potatos_list:
        if func(potato):
            result.append(potato)
    return result


def filter_foo(potato: str) -> bool:
    return "гнил" not in potato.lower()


good_potato = potato_filter(filter_foo, potatos)
print(good_potato)

############ Встроенный в пайтон фильтр

good_potatos = list(filter(filter_foo, potatos))
print(good_potatos)
good_potatos = list(filter(lambda potato: "гнил" not in potato.lower(), potatos))
print(good_potatos)

good_potatos = [potato for potato in potatos if "гнил" not in potato.lower()]
print(good_potatos)

good_potatos = []
for potato in potatos:
    if "гнил" not in potato.lower():
        good_potatos.append(potato)


##### ФИЛЬТРУЕМ И ЧИСТИМ

potatos = [
    "картошка",
    "картошка",
    "картошка",
    "гнилая картошка",
    "картошка",
    "гнилая картошка",
    "картошка",
    "картошка",
]

#! Фильтруем
good_potatos = list(filter(lambda potato: "гнил" not in potato.lower(), potatos))
print(good_potatos)

#! Чистим
good_clean_potatos = list(map(potato_cleaner, good_potatos))
print(good_clean_potatos)

#! Фильтруем и чистим
good_clean_potatos = list(
    map(
        lambda potato: potato + "почищено",
        filter(lambda potato: "гнил" not in potato.lower(), potatos),
    )
)
print(good_clean_potatos)


#! Функция sorted
"""
#? Функция sorted
Создана для того чтобы сортировать коллекции, передавая в нее функцию-компаратор.
Как помогатор из фиксиков)
НАПРИМЕР
Вы хотите отсортировать коллекцию имен по алфавиту по последней букве
Вы можете написать лямбду которая примет имя и вернет последнюю букву!
"""

names = [
    "Антон",
    "Братислав",
    "Владимир",
    "Борис",
    "Андрей",
    "Аркадий",
    "Валентин",
    "Анна",
    "Алина",
]

#? Сортируем по последней букве алфавита
sorted_last_letter = list(sorted(names, key=lambda name: name[-1]))
print(sorted_last_letter)


#! Sorted, Callable, Практика с коллекциями, Генераторы?