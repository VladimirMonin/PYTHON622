from typing import Literal, Annotated, NotRequired, TypedDict
from pydantic import BaseModel, Field

# Этот код не гарантирует никаких проверок. Он подсказывает, что в этой переменной категория может являться одной из этих двух строк — это подсказка типов. Однако когда она помещается в Pydantic, она становится частью проверок.
Сategory = Literal["хот-дог", "не хот-дог"]
Price = Annotated[float, "цена", (199.99, 299.89)]

# Здесь мы создали переменную и сказали, что она имеет свой собственный тип данных, который мы только что придумали. Если попытаться поместить туда то, что противоречит этому типу данных, мы получаем подчёркивание в редакторе. Но это не будет означать, что код не будет работать: это просто редактор подсказывает, что что-то не так с этим значением. При этом код исполняться будет.
category_1: Сategory = "чебурек"


# Здесь мы делаем то же самое, но помещаем наш свежесозданный тип данных в модель Pydantic. И теперь модель Pydantic будет проверять эти значения на соответствие. Если туда попадёт что-то кроме тех двух `Literal`, которые мы указали, мы получим `ValidationError` от Pydantic.
# class Food(BaseModel):
#     category: Сategory


# cheburek = Food(category="чебурек")

"""pydantic_core._pydantic_core.ValidationError: 1 validation error for Food
category
  Input should be 'хот-дог' or 'не хот-дог' [type=literal_error, input_value='чебурек', input_type=str]
"""

class Food(BaseModel):
    name: str
    category: Сategory
    price: Price


Ingredients = Literal["грибы", "картошка", "халапенью", "морковка по-корейски", "дополнительный соус"]

class Shaverma(BaseModel):
    name: str
    price: Price
    ingredients: list[Ingredients] | None = Field(default=None, min_length=1, max_length=6)



print(Price.__origin__) # <class 'float'>
print(Price.__metadata__) # ('цена', (199.99, 299.89))
print(Price.__metadata__[0]) # цена

food_1 = Food(name="Хот-дог классический", category="хот-дог", price=200)


# shaverma_1 = Shaverma(name="Богатырь", price=500, ingredients=["котята"])
shaverma_1 = Shaverma(name="Богатырь", price=500, ingredients=["грибы"])
"""pydantic_core._pydantic_core.ValidationError: 1 validation error for Shaverma
ingredients.0
  Input should be 'грибы', 'картошка', 'халапенью', 'морковка по-корейски' or 'дополнительный соус' [type=literal_error, input_value='котята', input_type=str]"""


shaverma = {"name": "Классика", "price": 250}

"""
Python про него знает только одно: это dict. Редактор подсказывает вам методы словаря — keys, values, get — и ничего про содержимое. Какой ключ правильный: name или title? price или cost? Приходится помнить, а опечатку shaverma["prise"] вы увидите только при запуске, да и то как KeyError.

TypedDict — это способ записать список ключей и их типы как отдельный тип:
"""

class ShavermaDict(TypedDict):
    name: str
    price: float
    ingredients: NotRequired[list[Ingredients] | None]


shaverma: ShavermaDict = {"name": "Малышка", "price": 300}
print(shaverma["name"])

"""
Ключевой момент: чем это отличается от обычной аннотации типов данных в Python? Это словарь с ключами-строками и значениями — строкой или числом. Смысл в том, что здесь мы явно обозначаем названия ключей и их типы данных.

Поэтому редактор нам всегда будет подсказывать названия ключей и их типы данных, когда мы набираем подобные словари или когда мы к ним обращаемся. Что может быть очень удобно при разработке.
"""

###################################### ЧАСТЬ 2 
raw_order: ShavermaDict = {
    "name": "Классика",
    "price": 220,
    "ingredients": ["картошка", "морковка по-корейски"]
}

print(raw_order)
order = Shaverma(**raw_order)
print(order)