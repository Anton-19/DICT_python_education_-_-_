import random


def add_friends():
    try:
        num_people = int(input("Enter the number of people joining (including you): > "))  # Зчитуємо кількість людей
    except ValueError:
        print("Please enter a valid number.")
        return None

    if num_people <= 0:                           # Якщо кількість людей некоректна, виводимо повідомлення
        print("No one is joining for the party")
        return None

    friends_dict = {}                     # Створюємо порожній словник для збереження імен друзів

    for i in range(num_people):
        name = input(f"Enter the name of person {i + 1}: > ")
        friends_dict[name] = 0

    return friends_dict


def split_bill(friends_dict):
    if not friends_dict:
        return

    try:
        total_amount = float(input("Enter the total amount: > "))     # Зчитуємо загальну суму рахунку
    except ValueError:
        print("Please enter a valid amount.")
        return

    num_people = len(friends_dict)  # Кількість учасників


    lucky_choice = input("Do you want to pick a lucky one? (Yes/No): > ").strip().lower()       # Питаємо користувача, чи хоче він вибрати щасливчика

    if lucky_choice == 'yes':
        lucky_person = random.choice(list(friends_dict.keys()))        # Випадковий вибір щасливчика
        print(f"{lucky_person} is the lucky one!")


        amount_per_person = round(total_amount / (num_people - 1), 2)        # Оновлюємо суму на кожного, крім щасливчика

        for name in friends_dict:
            if name == lucky_person:
                friends_dict[name] = 0
            else:
                friends_dict[name] = amount_per_person
    else:
        print("No one is going to be lucky.")


        amount_per_person = round(total_amount / num_people, 2)      # Розподіляємо загальну суму порівну між усіма учасниками
        for name in friends_dict:
            friends_dict[name] = amount_per_person

    print(friends_dict)                       # Виводимо оновлений словник

friends_dict = add_friends()            # Додаємо друзів

if friends_dict:                        # Перевіряємо, чи були додані друзі
    split_bill(friends_dict)           # Ділимо рахунок
