import random


# Функція генерує арифметичне завдання або число для зведення в квадрат
def generate(level):
    if level == 1:        # Простий рівень, операції +, -, * з числами 2-9
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        return f"{num1} {operation} {num2}", eval(f"{num1} {operation} {num2}")
    elif level == 2:        # Складний рівень, зведення чисел 11-29 у квадрат
        num = random.randint(11, 29)
        return f"{num}", num ** 2


# Функція перевіряє формат вводу
def getanswer():
    while True:
        try:
            return int(input("> "))
        except ValueError:
            print("Incorrect format.")


# Головна фнкція
def main():
    while True:
        try:
            level = int(input(
                "> Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> "))
            if level in [1, 2]:
                break
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

    correct_answers = 0  # Підрахунок прав відповідей

    for _ in range(5):
        question, correct_answer = generate(level)
        print(f"> {question}")
        user_answer = getanswer()

        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    # Вивід результату
    print(f"Your mark is {correct_answers}/5.")

    # Запит на збереження результату у файл
    save_result = input("> Would you like to save your result to the file? Enter yes or no.\n> ").strip().lower()
    if save_result in ["yes", "y"]:
        name = input("> What is your name?\n> ").strip()
        level_desc = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"

        # Запис результату у файл
        with open("results.txt", "a") as file:
            file.write(f"{name}: {correct_answers}/5 in level {level} ({level_desc}).\n")
        print("The results are saved in \"results.txt\".")


# Запуск програми
if __name__ == "__main__":
    main()
