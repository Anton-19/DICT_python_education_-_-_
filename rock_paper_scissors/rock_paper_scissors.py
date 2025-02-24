# Словник, що містить виграшні ходи
win_moves = {
    "rock": "paper",     # Камінь -> Папір
    "paper": "scissors", # Папір -> Ножиці
    "scissors": "rock"   # Ножиці -> Камінь
}

# Отримуємо вибір користувача
user_choice = input("Enter your choice (rock, paper, scissors):> ").strip().lower()

# Перевіряємо, чи правильний ввід
if user_choice in win_moves:
    computer_choice = win_moves[user_choice]  # Визначаємо виграшний хід комп'ютера
    print(f"Sorry, but the computer chose {computer_choice}")
else:
    print("Invalid input. Please enter rock, paper, or scissors.")
