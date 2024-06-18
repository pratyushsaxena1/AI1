import sys

def determine_winner(board):
    if board[0] == board[1] == board[2] and board[0] == "X":
        return 1
    elif board[3] == board[4] == board[5] and board[3] == "X":
        return 1
    elif board[6] == board[7] == board[8] and board[6] == "X":
        return 1
    elif board[0] == board[3] == board[6] and board[0] == "X":
        return 1
    elif board[1] == board[4] == board[7] and board[1] == "X":
        return 1
    elif board[2] == board[5] == board[8] and board[2] == "X":
        return 1
    elif board[0] == board[4] == board[8] and board[0] == "X":
        return 1
    elif board[2] == board[4] == board[6] and board[2] == "X":
        return 1
    elif board[0] == board[1] == board[2] and board[0] == "O":
        return -1
    elif board[3] == board[4] == board[5] and board[3] == "O":
        return -1
    elif board[6] == board[7] == board[8] and board[6] == "O":
        return -1
    elif board[0] == board[3] == board[6] and board[0] == "O":
        return -1
    elif board[1] == board[4] == board[7] and board[1] == "O":
        return -1
    elif board[2] == board[5] == board[8] and board[2] == "O":
        return -1
    elif board[0] == board[4] == board[8] and board[0] == "O":
        return -1
    elif board[2] == board[4] == board[6] and board[2] == "O":
        return -1
    elif board.find(".") == -1:
        return 0
    else:
        return None
    
def make_new_board(board, index, insertion):
    return board[:index] + insertion + board[index + 1:]

def get_possible_boards(board, player):
    return [make_new_board(board, index, player) for index, space in enumerate(board) if space == '.']

def display_board(board):
    print("\n" + board[0] + " | " + board[1] + " | " + board[2] + "\n" + "--|---|--" + "\n" + board[3] + " | " + board[4] + " | " + board[5] + "\n" + "--|---|--" + "\n" + board[6] + " | " + board[7] + " | " + board[8] + "\n")

def max_step(board):
    end_result = determine_winner(board)
    if end_result is not None:
        return end_result
    return max([min_step(possible_board) for possible_board in get_possible_boards(board, 'X')])

def min_step(board):
    end_result = determine_winner(board)
    if end_result is not None:
        return end_result
    return min([max_step(possible_board) for possible_board in get_possible_boards(board, 'O')])

def make_move(board, user):
    value, index = (-2, -1) if user == 'X' else (2, -1)
    outcomes_dict = {-1: "lose", 0: "tie", 1: "win"} if user == 'X' else {1: "lose", 0: "tie", -1: "win"}
    for possible_board in get_possible_boards(board, user):
        element_comparisons, game_outcome = [board[i] != possible_board[i] for i in range(9)].index(True), min_step(possible_board) if user == 'X' else max_step(possible_board)
        print(f"Moving at {element_comparisons} results in a {outcomes_dict[game_outcome]}.")
        if (user == 'X' and game_outcome > value) or (user == 'O' and game_outcome < value):
            value, index = game_outcome, element_comparisons
    print("\nI choose space " + str(index) + "\n\nCurrent board:")
    display_board(make_new_board(board, index, user))
    return make_new_board(board, index, user)

def user_turn(board):
    end_result = determine_winner(board)
    if end_result is not None:
        return board, end_result
    print(f"You can move to any of these spaces: {[i for i in range(9) if board[i] == '.']}.")
    index = int(input("Your choice? "))
    display_board(make_new_board(board, index, user))
    return computer_turn(make_new_board(board, index, user))

def computer_turn(board):
    end_result = determine_winner(board)
    if end_result is not None:
        return board, end_result
    return user_turn(make_move(board, computer))

board = sys.argv[1]
display_board(board)
if board.count(".") == 9:
    computer = input("Should I be X or O? ")
    if computer == 'X':
        user = 'O' 
    else:
        user = 'X'
    print("\nCurrent board:")
    display_board(board)
else:
    if board.count("X") == board.count("O"):
        computer, user = 'X', 'O' 
    else:
        computer, user = 'O', 'X'
board, winner = computer_turn(board) if computer == 'X' else user_turn(board)
print("I win!" if winner == 1 or winner == -1 else "We tied!")