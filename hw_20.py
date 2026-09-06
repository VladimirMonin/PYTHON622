try:
    from cities import cities_list
except:
    print("Файл не обнаружен")
    exit()

cities_set = {city["name"] for city in cities_list}

computer_city = ""
round_count = 0

while True:
    # Начало хода челвоека
    user_city = input("Введите город: ")

    # ПРОВЕРКИ ХОДА ЧЕЛОВЕКА
    # 1. Город есть в сете
    if user_city not in cities_set:
        print(f"Города {user_city} нет в списке")
        print(f"Ты проиграл, человек! Му-ха-ха!!!")
        break

    # 2. Соответствие условиям правила игры
    # 2.1 Проверка что компьютер вообще называл что-то (НЕ первый ход)
    if computer_city:
        # 2.2 Проверка правил
        if user_city[0].lower() != computer_city[-1]:
            print(f"Города {user_city} и {computer_city} не подходят")
            print(f"Ты проиграл, человек! Му-ха-ха!!!")
            break

    # 3. User city годный вариант. Мы удаляем город из сета
    cities_set.remove(user_city)

    # ХОД КОМПЬЮТЕРА

    # Компьютер обходит циклом набор городов и ищет подходящий
    for city in cities_set:
        # Проверка на правила игры
        if city[0].lower() == user_city[-1]:
            # Назначение переменной
            computer_city = city
            print(f"Компьютер выбрал город: {computer_city}")
            # Удаляем город из сета
            cities_set.remove(computer_city)
            break
    else:
        print("Я не дооценил тебя человек! Твой интеллект превзошел меня!!!!")
