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

def max_step(board):
    global count
    temp_set = set()
    end_result = determine_winner(board)
    if end_result is not None:
        return end_result
    for possible_board in get_possible_boards(board, 'X'):
        temp_set.add(max_step(possible_board))
        count += 1
        boards_set.add(possible_board)
    return max(temp_set)

def min_step(board):
    global count
    temp_set = set()
    end_result = determine_winner(board)
    if end_result is not None:
        return end_result
    for possible_board in get_possible_boards(board, 'O'):
        temp_set.add(min_step(possible_board))
        count += 1
        boards_set.add(possible_board)
    return min(temp_set)

def main():
    global boards_set
    boards_set = set()
    max_step('.........')
    
    x_wins_5_steps = 0
    x_wins_7_steps = 0
    x_wins_9_steps = 0
    o_wins_6_steps = 0
    o_wins_8_steps = 0
    draws = 0

    for board in boards_set:
        result = determine_winner(board)
        x_moves = board.count('X')
        o_moves = board.count('O')

        if x_moves == 5:
            x_wins_5_steps += 1
        elif x_moves == 7:
            x_wins_7_steps += 1
        elif x_moves == 9 and result == 1:
            x_wins_9_steps += 1

        if o_moves == 6 and result == -1:
            o_wins_6_steps += 1
        elif o_moves == 8 and result == -1:
            o_wins_8_steps += 1

        if x_moves + o_moves == 9:
            if result == 0:
                draws += 1

    print("X wins in 5 steps:", x_wins_5_steps)
    print("X wins in 7 steps:", x_wins_7_steps)
    print("X wins in 9 steps:", x_wins_9_steps)
    print("O wins in 6 steps:", o_wins_6_steps)
    print("O wins in 8 steps:", o_wins_8_steps)
    print("Draws:", draws)

main()
