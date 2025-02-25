import random


# Функція генерує арифметичне завдання або число для зведення в квадрат
def generate(level):
    if level == 1:               # Прос. рівень, операції +, -, * з числами 2-9
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        return f"{num1} {operation} {num2}", eval(f"{num1} {operation} {num2}")
    elif level == 2:             # Складний рівень, зведення чисел 11-29 у квадрат
        num = random.randint(11, 29)
        return f"{num}", num ** 2


# Функція запитує рівень складності у користувача
def choose_level():
    while True:
        try:
            level = int(input(
                "> Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> "))
            if level in [1, 2]:
                return level       # Коректний вибір
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")


# Функція запитує відповідь користувача та перевіряє формат введення
def get_user():
    while True:
        try:
            return int(input("> "))
        except ValueError:
            print("Incorrect format.")


# Функція проводить тест і підраховує правильні відповіді
def run_test(level):
    correct_answers = 0        # Лічильник првильних відповідей
    for _ in range(5):
        question, correct_answer = generate(level)
        print(f"> {question}")
        user_answer = get_user()

        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1  # Збільшуємо лічильник правильних відповідей
        else:
            print("Wrong!")
    return correct_answers


# Функція для збереження результатів у файл
def save_result(correct_answers, level):
    save_result = input("> Would you like to save your result to the file? Enter yes or no.\n> ").strip().lower()
    if save_result in ["yes", "y"]:
        name = input("> What is your name?\n> ").strip()
        level_desc = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"

        # Запис результату у файл
        with open("results.txt", "a") as file:
            file.write(f"{name}: {correct_answers}/5 in level {level} ({level_desc}).\n")
        print("The results are saved in \"results.txt\".")


# Функція програми
def main():
    level = choose_level()
    correct_answers = run_test(level)
    print(f"Your mark is {correct_answers}/5.")
    save_result(correct_answers, level)


# Запуск програми
if __name__ == "__main__":
    main()

