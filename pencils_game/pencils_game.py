import random

# Функція для отримання коректного числа олівців
def get_initial_pencils():
    while True:
        pencils = input("How many pencils would you like to use:> ")
        if not pencils.isdigit() or int(pencils) <= 0:
            if not pencils.isdigit() or int(pencils) < 0:
                print("The number of pencils should be numeric")
            elif int(pencils) == 0:
                print("The number of pencils should be positive")
        else:
            return int(pencils)

# Функція для визначення, хто починає першим
def get_first_player(name1, name2):
    while True:
        first_player = input(f"Who will be the first ({name1}, {name2}):> ")
        if first_player != name1 and first_player != name2:
            print(f"Choose between '{name1}' and '{name2}'")
        else:
            return first_player

# Функція для ходу бота
def bot_move(pencils):
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:
        return random.randint(1, 3,)  # Випадковий хід у програшній позиції

# Основна функція гри
def pencils_game():
    pencils = get_initial_pencils()  # Запитуємо початкову кількість олівців
    players = ["John", "Jack"]        # "Jack"  бот
    current_player = get_first_player(players[0], players[1])         # Визначаємо першого гравця

    while pencils > 0:
        print('|' * pencils)  # Виводимо олівці у вигляді '|'
        print(f"{current_player}'s turn!")

        if current_player == "Jack":
            taken = bot_move(pencils)
            print(taken)
        else:
            while True:
                try:
                    taken = int(input("> "))
                    if taken not in [1, 2, 3]:
                        print("Possible values: '1', '2' or '3'")
                    elif taken > pencils:
                        print("Too many pencils were taken")
                    else:
                        break
                except ValueError:
                    print("Possible values: '1', '2' or '3'")

        # Віднімаємо взяті олівці від загальної кількості
        pencils -= taken

        # Визначаємо наступного гравця
        if pencils > 0:
            current_player = players[1] if current_player == players[0] else players[0]

    # Виведення переможця
    winner = players[1] if current_player == players[0] else players[0]
    print(f"{winner} won!")

# Запуск гри
pencils_game()