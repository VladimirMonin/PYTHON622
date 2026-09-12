


# assert 

assert 2 == 2
# assert 2 == 3, "Кажется два это не три"

favorite_dish = "пицца"

assert len(favorite_dish) == 5, "Кажется что пицца состоит НЕ из 5 букв"


name = "Михаил"
assert name == "Михаил", "Упс, кажется name НЕ РАВНО Роман"

if name != "Михаил":
    raise AssertionError("Упс, кажется name НЕ РАВНО Роман")


def get_hello_msg(name: str)->str:
    return f"Привет {name}"



test_data_get_hello_names = [
    ["Никита", "Привет Никита"],
    ["Михаил", "Привет Михаил"],
    ["Ирина", "Привет Ирина"]
]

import pytest

@pytest.mark.parametrize("name, expected", test_data_get_hello_names)
def test_get_hello_msg(name: str, expected: str):
    assert get_hello_msg(name) == expected, f"Ожидалось {expected}"


test_data_get_sum = [
    [2, 2, 4],
    [3, 4, 7],
    [5, 6, 11],
    [10, 10, 22]
]

def get_sum(a: int, b: int) -> int:
    return a + b

@pytest.mark.parametrize("a, b, expected", test_data_get_sum)
def test_get_sum(a: int, b: int, expected: int):
    assert get_sum(a, b) == expected, f"Ожидалось {expected}"
