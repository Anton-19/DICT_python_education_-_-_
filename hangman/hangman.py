import random
import string

# Створюємо список слів
word_list = ['python', 'java', 'javascript', 'php']

# Функція для вибору випадкового слова
def get_random_word():
    return random.choice(word_list).lower()

# Функція для виведення поточного стану слова
def display_word(guessed_word):
    return ' '.join(guessed_word)

# Функція для перевірки введення користувача
def is_valid_input(guess):
    if len(guess) != 1:  # Перевіряємо, чи введено рівно одну літеру
        print("You should input a single letter")
        return False
    if guess not in string.ascii_lowercase:  # Перевірка, чи це мала англійська літера
        print("Please enter a lowercase English letter")
        return False
    return True

# Функція для однієї гри
def play_game():
    secret_word = get_random_word()
    guessed_word = ['_'] * len(secret_word)  # Слово для виведення з пробілами
    attempts_left = 8  # Кількість життів (помилок)
    used_letters = []  # Літери, які вже були використані

    # Виведення початкового стану гри
    print("HANGMAN")
    print(f"Word: {display_word(guessed_word)}")
    print(f"Attempts left: {attempts_left}")

    # Основний цикл гри
    while attempts_left > 0 and '_' in guessed_word:
        guess = input("Input a letter: > ").lower()

        # Перевірка коректності введення
        if not is_valid_input(guess):
            continue

        # Перевірка, чи вже введена така літера
        if guess in used_letters:
            print("You've already guessed this letter")
            continue

        # Додаємо літеру до списку використаних
        used_letters.append(guess)

        # Перевіряємо, чи є літера в слові
        if guess in secret_word:
            previous_state = guessed_word.copy()  # Зберігаємо попередній стан слова

            # Розкриваємо всі зустрічі літери у слові
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[index] = guess

            # Якщо після введення стан слова не змінився, то це "No improvements"
            if previous_state == guessed_word:
                print("No improvements")
            else:
                print(f"Good job! The letter '{guess}' is in the word.")
        else:
            # Якщо літери немає у слові
            print("That letter doesn't appear in the word")
            attempts_left -= 1

        # Виведення поточного стану гри
        print(f"Word: {display_word(guessed_word)}")
        print(f"Used letters: {', '.join(used_letters)}")
        print(f"Attempts left: {attempts_left}")

    # Перевірка результату гри
    if '_' not in guessed_word:
        print("You guessed the word!")
        print("You survived!")
    else:
        print(f"You lost! The word was '{secret_word}'. Better luck next time!")

# Головне меню
def main_menu():
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ').lower()
        if choice == 'play':
            play_game()
        elif choice == 'exit':
            print("Goodbye!")
            break
        else:
            print('Invalid input. Please type "play" to start the game or "exit" to quit.')

# Запуск головного меню
main_menu()