board = ['-','-','-',
         '-','-','-',
         '-','-','-']

game_not_finished = True

winner = None

current_player = 'X'


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    display_board()

    #game still ongoing
    while game_not_finished:
        handle_turn(current_player)
        check_game_end()
        change_player()
    # game end
    if winner == 'X' or winner == 'O':
        print(winner + " won.")
    elif winner == None:
        print("Tie")


def check_game_end():
    check_win()
    check_tie()

def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return

def check_rows():
    global game_not_finished
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_not_finished = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_not_finished
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_not_finished = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_not_finished
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    if diagonals_1 or diagonals_2:
        game_not_finished = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]

    return

def check_tie():
    global game_not_finished
    if '-' not in board:
        game_not_finished = False
    return

def change_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose your position from 1-9: ")

    valid = False
    while not valid:

        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input("Choose a position from 1-9: ")


        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print("You cant go there. Go again!")




    board[position] = player

    display_board()

play_game()
