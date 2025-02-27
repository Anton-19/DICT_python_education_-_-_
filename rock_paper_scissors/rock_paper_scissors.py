import random
import os

RATING_FILE = "rating.txt"

def read_ratings():
    #Читає рейтинг із файлу
    ratings = {}
    if os.path.exists(RATING_FILE):
        with open(RATING_FILE, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2 and parts[1].isdigit():
                    name, score = parts
                    ratings[name] = int(score)
    return ratings

def write_ratings(ratings):
    # записує рейтинг у файл
    with open(RATING_FILE, "w") as file:
        for name, score in ratings.items():
            file.write(f"{name} {score}\n")

def ask_name(ratings):
    # Запитує ім'я користувача і отримує його рахунок
    user_name = input("Enter your name: ").strip()
    print(f"Hello, {user_name}")
    return user_name, ratings.get(user_name, 0)

def ask_options():
    # Запитує список знаків для гри
    user_input = input("Enter options separated by commas (or press Enter for default 15 options): ").strip()
    default_options = [
        "rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper",
        "sponge", "wolf", "tree", "human", "snake", "scissors", "fire"
    ]
    options = [opt.strip().lower() for opt in user_input.split(",") if opt.strip()] if user_input else default_options
    print("Okay, let's start.")
    return options

def make_win_list(options):
    # Стврлює список переможних ходів
    win_list = {}
    n = len(options)
    for i, choice in enumerate(options):
        win_list[choice] = options[i + 1: i + 1 + (n // 2)] + options[:(i + 1 + (n // 2)) % n]
    return win_list

def check_winner(user_choice, computer_choice, win_list):
    # Визначає результат гри
    if user_choice == computer_choice:
        return f"There is a draw ({computer_choice})", 50                                # Нічия
    elif computer_choice in win_list[user_choice]:
        return f"Well done. The computer chose {computer_choice} and failed", 100        # Перемога
    else:
        return f"Sorry, but the computer chose {computer_choice}", 0                     # Комп'ютер переміг

def game_loop(user_name, user_score, options, win_list, ratings):

    while True:
        user_choice = input("Enter your choice (!rating, !exit, or one of the options): ").strip().lower()

        if user_choice == "!exit":
            if ratings.get(user_name, 0) != user_score:  # Записуємо тільки якщо змінився
                ratings[user_name] = user_score
                write_ratings(ratings)
            print("Bye!")
            break

        if user_choice == "!rating":
            print(f"Your rating: {user_score}")
            continue

        if user_choice in options:
            computer_choice = random.choice(options)
            result_message, score = check_winner(user_choice, computer_choice, win_list)
            print(result_message)
            user_score += score
        else:
            print("Invalid input.")

# Запуск програми
ratings = read_ratings()
user_name, user_score = ask_name(ratings)
options = ask_options()
win_list = make_win_list(options)
game_loop(user_name, user_score, options, win_list, ratings)
