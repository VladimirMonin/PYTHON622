from typing import Literal
from pydantic import BaseModel

# Этот код не гарантирует никаких проверок. Он подсказывает, что в этой переменной категория может являться одной из этих двух строк — это подсказка типов. Однако когда она помещается в Pydantic, она становится частью проверок.
Сategory = Literal["хот-дог", "не хот-дог"]

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

food_1 = Food(name="Хот-дог классический", category="хот-дог")
food_2 = Food(name="Чебурек", category="не хот-дог")
food_3 = Food(name=f"Хот-Дог с сыром", category="хот-дог")

menu = [food_1, food_2, food_3]
hots = [f.name for f in menu if f.category == "хот-дог"]

def only(items: list[Food], c: Сategory)-> list[Food]:
    return [f for f in items if f.category == c]

only(menu, "не хот-дог")
only(menu, "хот-дог")