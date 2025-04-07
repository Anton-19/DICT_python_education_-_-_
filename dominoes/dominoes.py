import random

def create_domino_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]

def distribute_pieces(domino_set):
    random.shuffle(domino_set)
    return domino_set[:7], domino_set[7:14], domino_set[14:]

def find_starting_piece(player_pieces, computer_pieces):
    doubles = [p for p in player_pieces + computer_pieces if p[0] == p[1]]
    if doubles:
        start_piece = max(doubles)
        if start_piece in player_pieces:
            player_pieces.remove(start_piece)
            return start_piece, "computer"
        else:
            computer_pieces.remove(start_piece)
            return start_piece, "player"
    return None, None

def display_game_state(stock_pieces, computer_pieces, domino_snake, player_pieces, status):
    print("=" * 70)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}")
    print("".join(str(p) for p in domino_snake))
    print("\nYour pieces:")
    for i, piece in enumerate(player_pieces, 1):
        print(f"{i}:{piece}")
    print(f"Status: {status}")

def is_valid_move(piece, domino_snake, side):
    return piece[1] == domino_snake[0][0] or piece[0] == domino_snake[0][0] if side == "left" else piece[0] == domino_snake[-1][1] or piece[1] == domino_snake[-1][1]

def make_move(piece, domino_snake, side):
    if side == "left":
        domino_snake.insert(0, piece if piece[1] == domino_snake[0][0] else piece[::-1])
    else:
        domino_snake.append(piece if piece[0] == domino_snake[-1][1] else piece[::-1])

def player_turn(player_pieces, domino_snake, stock_pieces):
    while True:
        try:
            move = int(input("> "))
            if move == 0:
                if stock_pieces:
                    player_pieces.append(stock_pieces.pop())
                return
            index = abs(move) - 1
            if index >= len(player_pieces):
                raise ValueError
            piece = player_pieces[index]
            side = "left" if move < 0 else "right"
            if is_valid_move(piece, domino_snake, side):
                make_move(piece, domino_snake, side)
                player_pieces.pop(index)
                return
            print("Illegal move. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def compute_frequencies(pieces, domino_snake):
    freq = {i: 0 for i in range(7)}
    for p in pieces + domino_snake:
        freq[p[0]] += 1
        freq[p[1]] += 1
    return freq

def computer_turn(computer_pieces, domino_snake, stock_pieces):
    freq = compute_frequencies(computer_pieces, domino_snake)
    scored_pieces = sorted(computer_pieces, key=lambda p: freq[p[0]] + freq[p[1]], reverse=True)
    for piece in scored_pieces:
        for side in ["right", "left"]:
            if is_valid_move(piece, domino_snake, side):
                make_move(piece, domino_snake, side)
                computer_pieces.remove(piece)
                return
    if stock_pieces:
        computer_pieces.append(stock_pieces.pop())

def check_winner(player_pieces, computer_pieces, stock_pieces, domino_snake):
    if not player_pieces:
        return "player"
    if not computer_pieces:
        return "computer"
    if not stock_pieces and all(not is_valid_move(p, domino_snake, "left") and not is_valid_move(p, domino_snake, "right") for p in player_pieces + computer_pieces):
        return "draw"
    return None

def play_domino():
    domino_set = create_domino_set()
    player_pieces, computer_pieces, stock_pieces = distribute_pieces(domino_set)
    starting_piece, current_turn = find_starting_piece(player_pieces, computer_pieces)
    if starting_piece is None:
        print("No valid starting piece found. Restarting game...")
        return play_domino()
    domino_snake = [starting_piece]
    while True:
        display_game_state(stock_pieces, computer_pieces, domino_snake, player_pieces, f"{'Your turn' if current_turn == 'player' else 'Computer is about to make a move. Press Enter to continue...'}")
        if current_turn == "player":
            player_turn(player_pieces, domino_snake, stock_pieces)
            current_turn = "computer"
        else:
            input()
            computer_turn(computer_pieces, domino_snake, stock_pieces)
            current_turn = "player"
        winner = check_winner(player_pieces, computer_pieces, stock_pieces, domino_snake)
        if winner:
            display_game_state(stock_pieces, computer_pieces, domino_snake, player_pieces, f"{winner.capitalize()} wins!" if winner != "draw" else "The game is a draw!")
            break

play_domino()
