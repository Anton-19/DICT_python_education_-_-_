def display_board(state):
    print("---------")                                    # Функція для відображення ігрового поля
    for i in range(3):
        print(f"| {state[i * 3]} {state[i * 3 + 1]} {state[i * 3 + 2]} |")
    print("---------")

def get_cell_index(x, y):
    return (x - 1) * 3 + (y - 1)                        # Функція для перевірки та перетворення координат у індекс у рядку

def is_cell_empty(state, x, y):
    index = get_cell_index(x, y)
    return state[index] == "_"

def check_game_state(state):
    rows = [state[0:3], state[3:6], state[6:9]]                                  # Функція для перевірки стану гри
    cols = [state[0:9:3], state[1:9:3], state[2:9:3]]
    diags = [state[0] + state[4] + state[8], state[2] + state[4] + state[6]]

    x_wins = any(line == "XXX" for line in rows + cols + diags)
    o_wins = any(line == "000" for line in rows + cols + diags)

    x_count = state.count("X")
    o_count = state.count("0")
    empty_count = state.count("_")

    if x_wins:
        return "X wins"
    elif o_wins:
        return "0 wins"
    elif empty_count == 0:                   # Нічия
        return "Draw"

    else:
        return "Game not finished"                     # Гра продовжується

def play_game():
    state = "_________"                       # Початкове порожнє поле
    current_player = "X"                     # Перший гравець починає з "X"

    display_board(state)                   # Відображаємо порожнє поле

    while True:
                           # Запитуємо координати для ходу
        while True:
            try:
                x, y = map(int, input(f"Player {current_player}, Enter the coordinates (x y):> ").split())

                if x < 1 or x > 3 or y < 1 or y > 3:                       # Перевірка, що координати в межах 1-3
                    print("Coordinates should be from 1 to 3!")
                    continue

                if not is_cell_empty(state, x, y):                            # Перевірка обраної клітинки
                    print("This cell is occupied! Choose another one!")
                    continue

                index = get_cell_index(x, y)                                          # Якщо введення добре, оновлюємо стан поля
                state = state[:index] + current_player + state[index + 1:]
                break
            except ValueError:
                print("You should enter numbers!")
                continue

        display_board(state)                             # Показуємо поле після ходу

        result = check_game_state(state)             # Превірка стану гри після кожного ходу
        if result != "Game not finished":
            print(result)                        # Виводимо результат
            break

        current_player = "0" if current_player == "X" else "X"

play_game()                # Запускаємо гру
