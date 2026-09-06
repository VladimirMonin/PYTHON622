"""
Lesson 11 - Args, Kwargs
Ruff Mypy
"""


print("Один")
print("Один", "Два")
print("Один", "Два", "Три")

list_strings = ["Один", "Два", "Три"]
print(*list_strings)

print(list_strings[0], list_strings[1], list_strings[2])

for i in range(len(list_strings)):
    print(list_strings[i])


def my_sum(*numbers: int | float):
    print(type(numbers))
    return int(sum(numbers))


print(my_sum(1, 2, 3))


numbers = [1, 2, 3]
print(my_sum(*numbers))

# def request_openai(client: OpenAI, messages: list[dict], model: str) -> dict:
"""
Как и в случае с обычными параметрами в Python, когда вы объявляете функцию, эти параметры становятся доступны внутри функции при ее запуске, как обычные переменные  Одна звездочка и две звездочки не меняют этого свойства, за тем исключением, что одна звездочка упаковывает все бесконечное количество поданных позиционных аргументов в кортеж  А две звездочки упаковывают бесконечное количество кейворд аргументов в словарь, где название аргумента становится ключом, а значение аргумента становится значением, лежащим в словаре по этому ключу
"""

def request_openai(**params):
    print(type(params))
    print(params.keys())
    print(params.values())

request_openai(client="Косой", message="На связь не вышел!", model="Боди позитив!")
    
dict_params = {
    "client": "Косой",
    "message": "На связь не вышел!",
    "model": "Боди позитив!"
}

request_openai(**dict_params)


def request_openai_2(client: str, messages: list[dict], model: str) -> str:
    return(f"Клиент: {client}, Сообщения: {messages}, Модель: {model}")

dict_params2 = {
    "client": "OpenAI",
    "messages": [{"content": "Расскажи шутку"}],
    "model": "gpt-7.5"
}

print(request_openai_2(**dict_params2))


"""
Ниже приведен пример того, что происходит при распаковке словаря с параметрами в функцию. Эта функция не принимает множественные keyword arguments, но при этом мы без проблем можем распаковать словарь в неё при условии, что ключи словаря и имена аргументов функции полностью соответствуют друг другу. Внутри себя Python делает примерно то, что написано в строке ниже.
"""
# print(request_openai_2(client=dict_params2["client"], messages=dict_params2["messages"], model=dict_params2["model"]))