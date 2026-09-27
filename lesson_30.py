"""
Специальные методы в Python — это те методы, которые Python использует в специальных случаях. Например, при создании экземпляра класса, при попытке привести экземпляр класса к строковому или к булевому значению, при попытке получить длину экземпляра класса, при сравнении разных экземпляров на больше и меньше или при попытке сделать математическую операцию между экземплярами класса. И даже в тех случаях, когда вы пытаетесь экземпляр класса «запустить», получается, что специальные методы описывают поведение класса в кодовой среде.

__init__ - запускается при инициализации эклемпляра
__str__ - при принте или при приведении через str()
__len__ - при помещении в строенную функцию длины
__bool__ - при if или при приведении через bool()
__call__ - делает экземпляр класса вызываемым - может принимать аргументы

-------

Ниже представлен перечень специальных методов Python для основных математических операций:

__add__(self, other)` — сложение (`+`);
__sub__(self, other)` — вычитание (`-`);
__mul__(self, other)` — умножение (`*`);
__truediv__(self, other)` — деление (`/`);
__iadd__(self, other)` — сложение с присваиванием (`+=`);
__isub__(self, other)` — вычитание с присваиванием (`-=`);
__imul__(self, other)` — умножение с присваиванием (`*=`);
__itruediv__(self, other)` — деление с присваиванием (`/=`).

"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Prompt:
    def __init__(self, start_prompt: "PromptPart"):
        self.start_prompt = start_prompt
        self.prompts_parts = []

    def __str__(self):
        return f"Промпт состоящий из {len(self.prompts_parts)+1} частей. Общая длина в символах: {self.__len__()}"

    def __len__(self):
        """
        Возвращает длину в знаках всех промптов из списка + длину стартового промпта
        """
        return len(self.start_prompt) + sum([len(prompt) for prompt in self.prompts_parts])

    def __add__(self, other: "PromptPart")-> Prompt:
        self.prompts_parts.append(other)
        return self


class PromptPart:
    def __init__(self, text_prompt: str):
        self.text_prompt = text_prompt

    def __str__(self):
        return self.text_prompt

    def __len__(self):
        return len(self.text_prompt)

    def __add__(self, other: "PromptPart"):
        return 


SYSTEM_PROMPT = "Ты репетитор по Python. Никогда не говоришь готовых решений, но всегда рад разобрать задачи и код на похожих примерах. Стараешься объяснять простым понятным языком, используя mermaid диаграммы, аналогии офисной жизни и популярные примеры из интернета"

STYLE_PROMPT = "Мне нравятся mermeid диаграммы, таблицы и нормальный текст. Ненавижу перечени нумерованные списки и ненумерованные списки. Использование эмодзи 5 из 10. Юмор 6 из 10 Простые и понятные объяснения 10 из 10"

system_prompt_part = PromptPart(SYSTEM_PROMPT)

main_prompt = (Prompt(system_prompt_part))

style_prompt_part = PromptPart(STYLE_PROMPT)

main_prompt += style_prompt_part

print(main_prompt)
print(len(main_prompt))