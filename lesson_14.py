# Sorted, sort, ключ сортировки, lambda, практика работы с коллекциями

"""
Повторение.
Лямбда - анонимная функция.
"""

names = [" АнТон", "АлиНА", "вЛАДИмиР  ", "ВаЛенТиН  "]


def name_normalizer(name: str) -> str:
    """
    Функция нормализации имени. Убирает пробелы, приводит в порядок регистр
    :param name: имя
    :return: нормализованное имя
    """
    return name.strip().title()


names_normailized = list(map(name_normalizer, names))

names_normailized = list(map(lambda name: name.strip().title(), names))
print(names_normailized)

names_normailized_v_letter = list(
    filter(lambda name: "в" in name.lower(), names_normailized)
)
print(names_normailized_v_letter)


names_normailized = [name.strip().title() for name in names]
names_normailized_v_letter = [
    name.strip().title() for name in names if "в" in name.lower()
]

############# SORT, SORTED
"""
Отличия `sort()` и `sorted()`. Они очень схожи по функционалу: оба — инструменты для сортировки коллекций, и в Python действительно сделали два таких инструмента с похожими названиями.

Ключевое отличие заключается в том, что `sort()` является методом списка, в то же время как `sorted()` является функцией высшего порядка. Таким образом, хоть названия этих инструментов и похожи, они делают достаточно разные вещи.

`sort()` может принимать `key` для сортировки — для сложных сортировок непосредственно списков. В то же время `sorted()` — инструмент для сортировки уже любого типа коллекций в Python, и он тоже может принимать `key` для сложных вариантов.

Важно отметить, что `key` — это опциональный аргумент в обоих вариантах, и ключом обычно является функция. Здесь вы можете использовать как встроенные функции Python (допустим, `len`), так и самописные функции, которые берут один из элементов коллекции и возвращают так называемый признак сортировки.

Допустим, если вы хотите отсортировать список имён по последней букве, ваша функция должна принимать имя и возвращать последнюю букву этого имени. Если вы хотите через `sorted()` отсортировать список словарей, ваша функция должна принимать словарь и возвращать какой-то из его элементов (допустим, возраст сотрудника, год выхода фильма или население города).
"""

students = [
    "Монин Владимир Александрович",
    "Казанцев Михаил Романович",
    "Истомин Степан Алексеевич",
    "Дрягин Антон Константинович",
    "Даций Александр Вадимович",
    "Денисова Ирина Владимировна",
    "Троянский Данил Александрович",
    "Котова Виктория Романовна",
    "Одинцов Роман Сергеевич",
    "Гудков Евгений Олегович",
    "Рыльская Елена Святославовна",
    "Афанасьев Никита Юрьевич",
    "Халявин Арсений Андреевич",
    "Чередилина Анастасия Игоревна",
    "Зверьков Михаил Вячеславович",
    "Ульяницкая Ксения Васильевна",
    "Наседкина Алина Жумагуловна",
    "Наседкин Валентин Сергеевич",
    "Шаповал Владимир Павлович",
    "Овсепян Тагуи Амбарцумовна",
]

from pprint import pprint

students.sort()
pprint(students)

students.sort(reverse=True)
pprint(students)

students.sort(key=len)
pprint(students)

students.sort(key=lambda full_name: full_name.split()[1])
pprint(students)

students.sort(key=lambda full_name: len(full_name.split()[1]))
pprint(students)

# PRACTICE - Попробуйте сортировку по количеству буквы р в ФИО от БОЛЬШЕГО к МЕНЬШЕМУ
# :full_name.lower().count("р")
students.sort(key=lambda full_name: full_name.lower().count("р"))

# ПЕРЕПАКОВКА СТУДЕНТОВ В СПИСОК СЛОВАРЕЙ
students_data = []

for student in students:
    student_dict = {}
    student_dict["fio"] = student
    student_dict["fio_length"] = len(student)
    student_dict["r_count"] = student.lower().count("р")
    students_data.append(student_dict)

# pprint(students_data)

students_data = [
    {"fio": student, "fio_length": len(student), "r_count": student.lower().count("р")}
    for student in students
]

# pprint(students_data)

# Размещаем коллекцию cities.py рядом с своим кодом
from cities import cities_list

"""
Города в названии которых больше всего букв р
Топ 10
"""

# cities_list.sort(
#     key=lambda city_dict: city_dict["name"].lower().count("р"), reverse=True
# )
# pprint(cities_list[:10], sort_dicts=False)

########################################################

# SORTED - ФУНКЦИЯ высшего порядка - принемает функцию сортировщик
sorted_students = list(sorted(students))
# pprint(sorted_students)

sorted_cities = list(sorted(cities_list, key=lambda city_dict: city_dict["population"], reverse=True))
# pprint(sorted_cities[:10])


# Сортировка по ключу district
sorted_cities = list(sorted(cities_list, key=lambda city_dict: city_dict["district"]))
# pprint(sorted_cities[:100])


def key_district_population(city_dict: dict) -> tuple:
    return city_dict["district"], city_dict["population"]

# sorted_cities = list(sorted(cities_list, key=key_district_population))
# pprint(sorted_cities[:100])

sorted_cities = list(sorted(cities_list, key=lambda city_dict: (city_dict["district"], -city_dict["population"])))
# pprint(sorted_cities[:100])

"""
Необходимо сделать фильтрацию списка городов: отобрать дистрикт «Центральный». После чего необходимо сделать сортировку по двум признакам. Первичный признак сортировки — это субъект, вторичный признак сортировки — это население.

Для населения сделайте сортировку по убыванию. Таким образом, вы получите на выходе список словарей с городами Центрального округа России, где области будут отсортированы по алфавиту по возрастанию.

И внутри каждой области города будут отсортированы от наибольшего к наименьшему.
"""

central_district = list(filter(lambda city_dict: city_dict["district"] == "Центральный", cities_list))

sorted_central_cities = list(sorted(central_district, key=lambda city_dict: (city_dict["subject"], -city_dict["population"])))

pprint(sorted_central_cities)