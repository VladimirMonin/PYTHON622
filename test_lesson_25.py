


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

name1 = "Валентин"
name2 = "Алина"
name3 = "Тагуи"

def test_get_hello_msg_valentin():
    assert get_hello_msg(name1) == "Привет Валентин", "Кажется функция get_hello_msg НЕ работает"


def test_get_hello_msg_girls():
    assert get_hello_msg(name2) == "Привет Алина!", "Кажется функция get_hello_msg НЕ работает"
    # В каждой тестовой функции должен быть только один assert - при этом тут они могут оба работать, но если первый упадет, то второй НЕ БУДЕТ ПРОВЕРЯТСЯ!!!!!!!!!!!!!
    assert get_hello_msg(name3) == "Привет Тагуи", "Кажется функция get_hello_msg НЕ работает"