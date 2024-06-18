# Imports

import sys
import random
import copy

# Basic functions

def display_board(board):
    print()
    print(board["subboard_1"][0] + " | " + board["subboard_1"][1] + " | " + board["subboard_1"][2] + "     |     " + board["subboard_2"][0] + " | " + board["subboard_2"][1] + " | " + board["subboard_2"][2] + "     |     " + board["subboard_3"][0] + " | " + board["subboard_3"][1] + " | " + board["subboard_3"][2])
    print("--|---|--     |     --|---|--     |     --|---|--")
    print(board["subboard_1"][3] + " | " + board["subboard_1"][4] + " | " + board["subboard_1"][5] + "     |     " + board["subboard_2"][3] + " | " + board["subboard_2"][4] + " | " + board["subboard_2"][5] + "     |     " + board["subboard_3"][3] + " | " + board["subboard_3"][4] + " | " + board["subboard_3"][5])
    print("--|---|--     |     --|---|--     |     --|---|--")
    print(board["subboard_1"][6] + " | " + board["subboard_1"][7] + " | " + board["subboard_1"][8] + "     |     " + board["subboard_2"][6] + " | " + board["subboard_2"][7] + " | " + board["subboard_2"][8] + "     |     " + board["subboard_3"][6] + " | " + board["subboard_3"][7] + " | " + board["subboard_3"][8])
    print("--------------------------------------------------")
    print(board["subboard_4"][0] + " | " + board["subboard_4"][1] + " | " + board["subboard_4"][2] + "     |     " + board["subboard_5"][0] + " | " + board["subboard_5"][1] + " | " + board["subboard_5"][2] + "     |     " + board["subboard_6"][0] + " | " + board["subboard_6"][1] + " | " + board["subboard_6"][2])
    print("--|---|--     |     --|---|--     |     --|---|--")
    print(board["subboard_4"][3] + " | " + board["subboard_4"][4] + " | " + board["subboard_4"][5] + "     |     " + board["subboard_5"][3] + " | " + board["subboard_5"][4] + " | " + board["subboard_5"][5] + "     |     " + board["subboard_6"][3] + " | " + board["subboard_6"][4] + " | " + board["subboard_6"][5])
    print("--|---|--     |     --|---|--     |     --|---|--")
    print(board["subboard_4"][6] + " | " + board["subboard_4"][7] + " | " + board["subboard_4"][8] + "     |     " + board["subboard_5"][6] + " | " + board["subboard_5"][7] + " | " + board["subboard_5"][8] + "     |     " + board["subboard_6"][6] + " | " + board["subboard_6"][7] + " | " + board["subboard_6"][8])
    print("--------------------------------------------------")
    print(board["subboard_7"][0] + " | " + board["subboard_7"][1] + " | " + board["subboard_7"][2] + "     |     " + board["subboard_8"][0] + " | " + board["subboard_8"][1] + " | " + board["subboard_8"][2] + "     |     " + board["subboard_9"][0] + " | " + board["subboard_9"][1] + " | " + board["subboard_9"][2])
    print("--|---|--     |     --|---|--     |     --|---|--")
    print(board["subboard_7"][3] + " | " + board["subboard_7"][4] + " | " + board["subboard_7"][5] + "     |     " + board["subboard_8"][3] + " | " + board["subboard_8"][4] + " | " + board["subboard_8"][5] + "     |     " + board["subboard_9"][3] + " | " + board["subboard_9"][4] + " | " + board["subboard_9"][5])
    print("--|---|--     |     --|---|--     |     --|---|--")
    print(board["subboard_7"][6] + " | " + board["subboard_7"][7] + " | " + board["subboard_7"][8] + "     |     " + board["subboard_8"][6] + " | " + board["subboard_8"][7] + " | " + board["subboard_8"][8] + "     |     " + board["subboard_9"][6] + " | " + board["subboard_9"][7] + " | " + board["subboard_9"][8])
    print()

def get_subboard_winner(board):
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

def get_winner(board):
    key_list_x = []
    key_list_o = []
    games_finished = 0
    for key in board:
        winner = get_subboard_winner(board[key])
        if winner == 1:
            key_list_x.append(key)
            games_finished += 1
        elif winner == -1:
            key_list_o.append(key)
            games_finished += 1
        elif winner == 0:
            games_finished += 1
    if "subboard_1" in key_list_x and "subboard_2" in key_list_x and "subboard_3" in key_list_x or "subboard_4" in key_list_x and "subboard_5" in key_list_x and "subboard_6" in key_list_x or "subboard_7" in key_list_x and "subboard_8" in key_list_x and "subboard_9" in key_list_x or "subboard_1" in key_list_x and "subboard_4" in key_list_x and "subboard_7" in key_list_x or "subboard_2" in key_list_x and "subboard_5" in key_list_x and "subboard_8" in key_list_x or "subboard_3" in key_list_x and "subboard_6" in key_list_x and "subboard_9" in key_list_x or "subboard_1" in key_list_x and "subboard_5" in key_list_x and "subboard_9" in key_list_x or "subboard_3" in key_list_x and "subboard_5" in key_list_x and "subboard_7" in key_list_x:
        return "X"
    elif "subboard_1" in key_list_o and "subboard_2" in key_list_o and "subboard_3" in key_list_o or "subboard_4" in key_list_o and "subboard_5" in key_list_o and "subboard_6" in key_list_o or "subboard_7" in key_list_o and "subboard_8" in key_list_o and "subboard_9" in key_list_o or "subboard_1" in key_list_o and "subboard_4" in key_list_o and "subboard_7" in key_list_o or "subboard_2" in key_list_o and "subboard_5" in key_list_o and "subboard_8" in key_list_o or "subboard_3" in key_list_o and "subboard_6" in key_list_o and "subboard_9" in key_list_o or "subboard_1" in key_list_o and "subboard_5" in key_list_o and "subboard_9" in key_list_o or "subboard_3" in key_list_o and "subboard_5" in key_list_o and "subboard_7" in key_list_o:
        return "O"
    elif games_finished == 9:
        return "Tie"
    else:
        return "None"

def is_valid_move(board, subboard, position):
    try:
        board_key = "subboard_" + str(subboard)
        if board[board_key][position - 1] == "." and get_subboard_winner(board[board_key]) == None:
            return True
    except:
        return False
    return False

def get_possible_moves(board, previous_move_index):
    moves = []
    if previous_move_index == None:
        for i in range(1, 10):
            winner = get_subboard_winner(board["subboard_" + str(i)])
            for index, position in enumerate(board["subboard_" + str(i)]):
                if position == "." and winner is None:
                    moves.append((i, index + 1))
    else: 
        for index, position in enumerate(board["subboard_" + str(previous_move_index)]):
            if position == "." and get_subboard_winner(board["subboard_" + str(previous_move_index)]) is None:
                moves.append((previous_move_index, index + 1))
    return moves

def update_board(board, move, piece):
    subboard, position = move
    board_key = "subboard_" + str(subboard)
    updated_board = copy.deepcopy(board)
    updated_board[board_key] = board[board_key][:(position - 1)] + str(piece) + board[board_key][position:]
    return updated_board

# User move

def get_user_move(board, previous_move_index):
    if previous_move_index is None:
        move_board = int(input("User, pick a board 1-9 to play a move in: "))
        move_position = int(input("Now, pick a position in that board 1-9: "))
        if is_valid_move(board, move_board, move_position):
            move = (move_board, move_position)
        else:
            print("That's an invalid move. Please try again.")
            move = get_user_move(board, previous_move_index)
    else:
        move_position = int(input("User, pick a position 1-9 in board " + str(previous_move_index) + ": "))
        if is_valid_move(board, previous_move_index, move_position):
            move = (previous_move_index, move_position)
        else:
            print("That's an invalid move. Please try again.")
            move = get_user_move(board, previous_move_index)
    return move

# Random move

def get_random_move(board, previous_move_index):
    if previous_move_index is None:
        subboard, position = random.randint(1, 9), random.randint(1, 9)
        if is_valid_move(board, subboard, position):
            move = (subboard, position)
        else:
            move = get_random_move(board, previous_move_index)
    else:
        possible_moves = get_possible_moves(board, previous_move_index)
        if len(possible_moves) == 0:
            previous_move_index = None
            move = get_random_move(board, previous_move_index)
        else:
            move = random.choice(possible_moves)
    return move

# Aggressive move

def get_aggressive_move(board, previous_move_index, token):
    if token == "X":
        correct_num = 1
    else:
        correct_num = -1
    if previous_move_index is None:
        move = get_random_move(board, previous_move_index)
    else:
        possible_moves = get_possible_moves(board, previous_move_index)
        if len(possible_moves) == 0:
            previous_move_index = None
            move = get_aggressive_move(board, previous_move_index, token)
        else:
            for possible_move in possible_moves:
                subboard, position = possible_move
                new_board = update_board(board, possible_move, token)
                if get_subboard_winner(new_board["subboard_" + str(subboard)]) == correct_num:
                    move = possible_move
                    break
                else:
                    move = get_random_move(board, previous_move_index)
    return move

# Best move

def get_best_move(board, previous_move_index, token):
    # Play 5, 1 if it's the first turn for the AI because no point in wasting all that time checking moves if it's the same outcome every time
    empty_tracker = 0
    for key in board:
        if board[key].count('.') != 9:
            empty_tracker += 1
    if empty_tracker == 0:
        return (5, 1)
    depth = 5
    return minimax(board, previous_move_index, token, depth)

def minimax(board, previous_move_index, token, depth):
    if token == 'X':
        max_number = float('-inf')
        max_move = (-1, -1)
        for possible_move in get_possible_moves(board, previous_move_index):
            _, possible_move_index = possible_move
            temp_board = update_board(board, possible_move, token)
            current_number = min_step(temp_board, possible_move_index, max_number, float('inf'), depth)
            if current_number > max_number:
                max_number = current_number
                max_move = possible_move
        return max_move
    else:
        min_number = float('inf')
        min_move = (-1, -1)
        for possible_move in get_possible_moves(board, previous_move_index):
            print(possible_move)
            _, possible_move_index = possible_move
            temp_board = update_board(board, possible_move, token)
            current_number = max_step(temp_board, possible_move_index, float('-inf'), min_number, depth)
            if current_number < min_number:
                min_number = current_number
                min_move = possible_move
        return min_move

def max_step(board, possible_move_index, alpha, beta, depth):
    if depth == 0:
        return grade_board(board, 'X')
    max_number = -1000000
    for possible_board in get_possible_boards(board, possible_move_index, 'X'):
        current_result = min_step(possible_board, possible_move_index, alpha, beta, depth - 1)
        # if current_result >= beta:
        #     return current_result
        # if current_result > alpha:
        #     alpha = current_result
        max_number = max(max_number, current_result)
        alpha = max(alpha, current_result)
        if alpha >= beta:
            break
    return max_number

def min_step(board, possible_move_index, alpha, beta, depth):
    if depth == 0:
        return grade_board(board, 'O')
    min_number = 1000000
    for possible_board in get_possible_boards(board, possible_move_index, 'O'):
        current_result = max_step(possible_board, possible_move_index, alpha, beta, depth - 1)
        # if alpha >= current_result:
        #     return current_result
        # if beta > current_result:
        #     beta = current_result
        min_number = min(min_number, current_result)
        beta = min(beta, current_result)
        if alpha >= beta:
            break
    return min_number

def get_possible_boards(board, previous_move_index, token):
    possible_boards = []
    for move_1 in get_possible_moves(board, previous_move_index):
        new_board_1 = board.copy()
        new_board_1 = update_board(new_board_1, move_1, token)
        possible_boards.append(new_board_1)
    return possible_boards

def grade_board(board, token):
    score = 0
    tokens = ['X', 'O']
    tokens.remove(token)
    enemy_token = tokens[0]
    overall_winner = get_winner(board)
    if overall_winner == token:
        score += 1000000000000000000000000000000000000000
    subboard_winners_list = []
    for key in board:
        subboard_winners_list.append(get_subboard_winner(board[key]))
    for w in subboard_winners_list:
        if w == token:
            score += 20
    # Center and corners
    if subboard_winners_list[4] == token:
        score += 10
    if subboard_winners_list[0] == token or subboard_winners_list[2] == token or subboard_winners_list[6] == token or subboard_winners_list[8] == token:
        score += 3
    # Two in a row with third empty
    if subboard_winners_list[0] == subboard_winners_list[1] == token and subboard_winners_list[2] == None or subboard_winners_list[1] == subboard_winners_list[2] == token and subboard_winners_list[0] == None or subboard_winners_list[0] == subboard_winners_list[2] == token and subboard_winners_list[1] == None:
        score += 15
    if subboard_winners_list[3] == subboard_winners_list[4] == token and subboard_winners_list[5] == None or subboard_winners_list[4] == subboard_winners_list[5] == token and subboard_winners_list[3] == None or subboard_winners_list[3] == subboard_winners_list[5] == token and subboard_winners_list[4] == None:
        score += 15
    if subboard_winners_list[6] == subboard_winners_list[7] == token and subboard_winners_list[8] == None or subboard_winners_list[7] == subboard_winners_list[8] == token and subboard_winners_list[6] == None or subboard_winners_list[6] == subboard_winners_list[8] == token and subboard_winners_list[7] == None:
        score += 15
    if subboard_winners_list[0] == subboard_winners_list[3] == token and subboard_winners_list[6] == None or subboard_winners_list[3] == subboard_winners_list[6] == token and subboard_winners_list[0] == None or subboard_winners_list[0] == subboard_winners_list[6] == token and subboard_winners_list[3] == None:
        score += 15
    if subboard_winners_list[1] == subboard_winners_list[4] == token and subboard_winners_list[7] == None or subboard_winners_list[4] == subboard_winners_list[7] == token and subboard_winners_list[1] == None or subboard_winners_list[1] == subboard_winners_list[7] == token and subboard_winners_list[4] == None:
        score += 15
    if subboard_winners_list[2] == subboard_winners_list[5] == token and subboard_winners_list[8] == None or subboard_winners_list[5] == subboard_winners_list[8] == token and subboard_winners_list[2] == None or subboard_winners_list[2] == subboard_winners_list[8] == token and subboard_winners_list[5] == None:
        score += 15
    if subboard_winners_list[0] == subboard_winners_list[4] == token and subboard_winners_list[8] == None or subboard_winners_list[4] == subboard_winners_list[8] == token and subboard_winners_list[0] == None or subboard_winners_list[0] == subboard_winners_list[8] == token and subboard_winners_list[4] == None:
        score += 15
    if subboard_winners_list[2] == subboard_winners_list[4] == token and subboard_winners_list[6] == None or subboard_winners_list[4] == subboard_winners_list[6] == token and subboard_winners_list[2] == None or subboard_winners_list[2] == subboard_winners_list[6] == token and subboard_winners_list[4] == None:
        score += 15
    # Two in a row with third occupied by enemy
    if subboard_winners_list[0] == subboard_winners_list[1] == token and subboard_winners_list[2] == enemy_token or subboard_winners_list[1] == subboard_winners_list[2] == token and subboard_winners_list[0] == enemy_token or subboard_winners_list[0] == subboard_winners_list[2] == token and subboard_winners_list[1] == enemy_token:
        score -= 20
    if subboard_winners_list[3] == subboard_winners_list[4] == token and subboard_winners_list[5] == enemy_token or subboard_winners_list[4] == subboard_winners_list[5] == token and subboard_winners_list[3] == enemy_token or subboard_winners_list[3] == subboard_winners_list[5] == token and subboard_winners_list[4] == enemy_token:
        score -= 20
    if subboard_winners_list[6] == subboard_winners_list[7] == token and subboard_winners_list[8] == enemy_token or subboard_winners_list[7] == subboard_winners_list[8] == token and subboard_winners_list[6] == enemy_token or subboard_winners_list[6] == subboard_winners_list[8] == token and subboard_winners_list[7] == enemy_token:
        score -= 20
    if subboard_winners_list[0] == subboard_winners_list[3] == token and subboard_winners_list[6] == enemy_token or subboard_winners_list[3] == subboard_winners_list[6] == token and subboard_winners_list[0] == enemy_token or subboard_winners_list[0] == subboard_winners_list[6] == token and subboard_winners_list[3] == enemy_token:
        score -= 20
    if subboard_winners_list[1] == subboard_winners_list[4] == token and subboard_winners_list[7] == enemy_token or subboard_winners_list[4] == subboard_winners_list[7] == token and subboard_winners_list[1] == enemy_token or subboard_winners_list[1] == subboard_winners_list[7] == token and subboard_winners_list[4] == enemy_token:
        score -= 20
    if subboard_winners_list[2] == subboard_winners_list[5] == token and subboard_winners_list[8] == enemy_token or subboard_winners_list[5] == subboard_winners_list[8] == token and subboard_winners_list[2] == enemy_token or subboard_winners_list[2] == subboard_winners_list[8] == token and subboard_winners_list[5] == enemy_token:
        score -= 20
    if subboard_winners_list[0] == subboard_winners_list[4] == token and subboard_winners_list[8] == enemy_token or subboard_winners_list[4] == subboard_winners_list[8] == token and subboard_winners_list[0] == enemy_token or subboard_winners_list[0] == subboard_winners_list[8] == token and subboard_winners_list[4] == enemy_token:
        score -= 20
    if subboard_winners_list[2] == subboard_winners_list[4] == token and subboard_winners_list[6] == enemy_token or subboard_winners_list[4] == subboard_winners_list[6] == token and subboard_winners_list[2] == enemy_token or subboard_winners_list[2] == subboard_winners_list[6] == token and subboard_winners_list[4] == enemy_token:
        score -= 20
    # Block three in a row for enemy
    if subboard_winners_list[0] == subboard_winners_list[1] == enemy_token and subboard_winners_list[2] == token or subboard_winners_list[1] == subboard_winners_list[2] == enemy_token and subboard_winners_list[0] == token or subboard_winners_list[0] == subboard_winners_list[2] == enemy_token and subboard_winners_list[1] == token:
        score += 30
    if subboard_winners_list[3] == subboard_winners_list[4] == enemy_token and subboard_winners_list[5] == token or subboard_winners_list[4] == subboard_winners_list[5] == enemy_token and subboard_winners_list[3] == token or subboard_winners_list[3] == subboard_winners_list[5] == enemy_token and subboard_winners_list[4] == token:
        score += 30
    if subboard_winners_list[6] == subboard_winners_list[7] == enemy_token and subboard_winners_list[8] == token or subboard_winners_list[7] == subboard_winners_list[8] == enemy_token and subboard_winners_list[6] == token or subboard_winners_list[6] == subboard_winners_list[8] == enemy_token and subboard_winners_list[7] == token:
        score += 30
    if subboard_winners_list[0] == subboard_winners_list[3] == enemy_token and subboard_winners_list[6] == token or subboard_winners_list[3] == subboard_winners_list[6] == enemy_token and subboard_winners_list[0] == token or subboard_winners_list[0] == subboard_winners_list[6] == enemy_token and subboard_winners_list[3] == token:
        score += 30
    if subboard_winners_list[1] == subboard_winners_list[4] == enemy_token and subboard_winners_list[7] == token or subboard_winners_list[4] == subboard_winners_list[7] == enemy_token and subboard_winners_list[1] == token or subboard_winners_list[1] == subboard_winners_list[7] == enemy_token and subboard_winners_list[4] == token:
        score += 30
    if subboard_winners_list[2] == subboard_winners_list[5] == enemy_token and subboard_winners_list[8] == token or subboard_winners_list[5] == subboard_winners_list[8] == enemy_token and subboard_winners_list[2] == token or subboard_winners_list[2] == subboard_winners_list[8] == enemy_token and subboard_winners_list[5] == token:
        score += 30
    if subboard_winners_list[0] == subboard_winners_list[4] == enemy_token and subboard_winners_list[8] == token or subboard_winners_list[4] == subboard_winners_list[8] == enemy_token and subboard_winners_list[0] == token or subboard_winners_list[0] == subboard_winners_list[8] == enemy_token and subboard_winners_list[4] == token:
        score += 30
    if subboard_winners_list[2] == subboard_winners_list[4] == enemy_token and subboard_winners_list[6] == token or subboard_winners_list[4] == subboard_winners_list[6] == enemy_token and subboard_winners_list[2] == token or subboard_winners_list[2] == subboard_winners_list[6] == enemy_token and subboard_winners_list[4] == token:
        score += 30
    # Repeat above logic within subboards
    for k in board:
        temp_board = board[k]
        # Center and corners
        if temp_board[4] == token:
            score += 5
        if temp_board[0] == token or temp_board[2] == token or temp_board[6] == token or temp_board[8] == token:
            score += 2
        # Two in a row with third empty
        if temp_board[0] == temp_board[1] == token and temp_board[2] == None or temp_board[1] == temp_board[2] == token and temp_board[0] == None or temp_board[0] == temp_board[2] == token and temp_board[1] == None:
            score += 3
        if temp_board[3] == temp_board[4] == token and temp_board[5] == None or temp_board[4] == temp_board[5] == token and temp_board[3] == None or temp_board[3] == temp_board[5] == token and temp_board[4] == None:
            score += 3
        if temp_board[6] == temp_board[7] == token and temp_board[8] == None or temp_board[7] == temp_board[8] == token and temp_board[6] == None or temp_board[6] == temp_board[8] == token and temp_board[7] == None:
            score += 3
        if temp_board[0] == temp_board[3] == token and temp_board[6] == None or temp_board[3] == temp_board[6] == token and temp_board[0] == None or temp_board[0] == temp_board[6] == token and temp_board[3] == None:
            score += 3
        if temp_board[1] == temp_board[4] == token and temp_board[7] == None or temp_board[4] == temp_board[7] == token and temp_board[1] == None or temp_board[1] == temp_board[7] == token and temp_board[4] == None:
            score += 3
        if temp_board[2] == temp_board[5] == token and temp_board[8] == None or temp_board[5] == temp_board[8] == token and temp_board[2] == None or temp_board[2] == temp_board[8] == token and temp_board[5] == None:
            score += 3
        if temp_board[0] == temp_board[4] == token and temp_board[8] == None or temp_board[4] == temp_board[8] == token and temp_board[0] == None or temp_board[0] == temp_board[8] == token and temp_board[4] == None:
            score += 3
        if temp_board[2] == temp_board[4] == token and temp_board[6] == None or temp_board[4] == temp_board[6] == token and temp_board[2] == None or temp_board[2] == temp_board[6] == token and temp_board[4] == None:
            score += 3
        # Two in a row with third occupied by enemy
        if temp_board[0] == temp_board[1] == token and temp_board[2] == enemy_token or temp_board[1] == temp_board[2] == token and temp_board[0] == enemy_token or temp_board[0] == temp_board[2] == token and temp_board[1] == enemy_token:
            score -= 4
        if temp_board[3] == temp_board[4] == token and temp_board[5] == enemy_token or temp_board[4] == temp_board[5] == token and temp_board[3] == enemy_token or temp_board[3] == temp_board[5] == token and temp_board[4] == enemy_token:
            score -= 4
        if temp_board[6] == temp_board[7] == token and temp_board[8] == enemy_token or temp_board[7] == temp_board[8] == token and temp_board[6] == enemy_token or temp_board[6] == temp_board[8] == token and temp_board[7] == enemy_token:
            score -= 4
        if temp_board[0] == temp_board[3] == token and temp_board[6] == enemy_token or temp_board[3] == temp_board[6] == token and temp_board[0] == enemy_token or temp_board[0] == temp_board[6] == token and temp_board[3] == enemy_token:
            score -= 4
        if temp_board[1] == temp_board[4] == token and temp_board[7] == enemy_token or temp_board[4] == temp_board[7] == token and temp_board[1] == enemy_token or temp_board[1] == temp_board[7] == token and temp_board[4] == enemy_token:
            score -= 4
        if temp_board[2] == temp_board[5] == token and temp_board[8] == enemy_token or temp_board[5] == temp_board[8] == token and temp_board[2] == enemy_token or temp_board[2] == temp_board[8] == token and temp_board[5] == enemy_token:
            score -= 4
        if temp_board[0] == temp_board[4] == token and temp_board[8] == enemy_token or temp_board[4] == temp_board[8] == token and temp_board[0] == enemy_token or temp_board[0] == temp_board[8] == token and temp_board[4] == enemy_token:
            score -= 4
        if temp_board[2] == temp_board[4] == token and temp_board[6] == enemy_token or temp_board[4] == temp_board[6] == token and temp_board[2] == enemy_token or temp_board[2] == temp_board[6] == token and temp_board[4] == enemy_token:
            score -= 4
        # Block three in a row for enemy
        if temp_board[0] == temp_board[1] == enemy_token and temp_board[2] == token or temp_board[1] == temp_board[2] == enemy_token and temp_board[0] == token or temp_board[0] == temp_board[2] == enemy_token and temp_board[1] == token:
            score += 8
        if temp_board[3] == temp_board[4] == enemy_token and temp_board[5] == token or temp_board[4] == temp_board[5] == enemy_token and temp_board[3] == token or temp_board[3] == temp_board[5] == enemy_token and temp_board[4] == token:
            score += 8
        if temp_board[6] == temp_board[7] == enemy_token and temp_board[8] == token or temp_board[7] == temp_board[8] == enemy_token and temp_board[6] == token or temp_board[6] == temp_board[8] == enemy_token and temp_board[7] == token:
            score += 8
        if temp_board[0] == temp_board[3] == enemy_token and temp_board[6] == token or temp_board[3] == temp_board[6] == enemy_token and temp_board[0] == token or temp_board[0] == temp_board[6] == enemy_token and temp_board[3] == token:
            score += 8
        if temp_board[1] == temp_board[4] == enemy_token and temp_board[7] == token or temp_board[4] == temp_board[7] == enemy_token and temp_board[1] == token or temp_board[1] == temp_board[7] == enemy_token and temp_board[4] == token:
            score += 8
        if temp_board[2] == temp_board[5] == enemy_token and temp_board[8] == token or temp_board[5] == temp_board[8] == enemy_token and temp_board[2] == token or temp_board[2] == temp_board[8] == enemy_token and temp_board[5] == token:
            score += 8
        if temp_board[0] == temp_board[4] == enemy_token and temp_board[8] == token or temp_board[4] == temp_board[8] == enemy_token and temp_board[0] == token or temp_board[0] == temp_board[8] == enemy_token and temp_board[4] == token:
            score += 8
        if temp_board[2] == temp_board[4] == enemy_token and temp_board[6] == token or temp_board[4] == temp_board[6] == enemy_token and temp_board[2] == token or temp_board[2] == temp_board[6] == enemy_token and temp_board[4] == token:
            score += 8

    # Make score negative if token O and return
    if token == 'O':
        score = score * -1
    return score

# Play game functions

def play_x_move(board, previous_move_index, first_player_type, second_player_type):
    display_board(board)
    if first_player_type == "USER":
        move = get_user_move(board, previous_move_index)
    elif first_player_type == "RANDOM":
        move = get_random_move(board, previous_move_index)
    elif first_player_type == "AGGRESSIVE":
        move = get_aggressive_move(board, previous_move_index, "X")
    elif first_player_type == "BEST":
        move = get_best_move(board, previous_move_index, "X")
    _, position = move
    board = update_board(board, move, "X")
    if board["subboard_" + str(position)].find(".") == -1 or get_subboard_winner(board["subboard_" + str(position)]) != None:
        previous_move_index = None
    else:
        previous_move_index = position
    winner = get_winner(board)
    if winner == "X":
        display_board(board)
        print("\nPlayer 1 wins!\n")
        sys.exit()
    elif winner == "Tie":
        display_board(board)
        print("\nIt's a tie!\n")
        sys.exit()
    play_o_move(board, previous_move_index, first_player_type, second_player_type)

def play_o_move(board, previous_move_index, first_player_type, second_player_type):
    display_board(board)
    if second_player_type == "USER":
        move = get_user_move(board, previous_move_index)
    elif second_player_type == "RANDOM":
        move = get_random_move(board, previous_move_index)
    elif second_player_type == "AGGRESSIVE":
        move = get_aggressive_move(board, previous_move_index, "O")
    elif second_player_type == "BEST":
        move = get_best_move(board, previous_move_index, "O")
    _, position = move
    board = update_board(board, move, "O")
    if board["subboard_" + str(position)].find(".") == -1 or get_subboard_winner(board["subboard_" + str(position)]) != None:
        previous_move_index = None
    else:
        previous_move_index = position
    winner = get_winner(board)
    if winner == "O":
        display_board(board)
        print("\nPlayer 2 wins!\n")
        sys.exit()
    elif winner == "Tie":
        display_board(board)
        print("\nIt's a tie!\n")
        sys.exit()
    play_x_move(board, previous_move_index, first_player_type, second_player_type)

def start_game():
    print("This game is called Ultimate Tic Tac Toe. Essentially, it's a Tic Tac Toe game, but every square has another Tic Tac Toe grid inside it. Players attempt to win three small boards in a row to win.")
    board = dict()
    board["subboard_1"] = "........."
    board["subboard_2"] = "........."
    board["subboard_3"] = "........."
    board["subboard_4"] = "........."
    board["subboard_5"] = "........."
    board["subboard_6"] = "........."
    board["subboard_7"] = "........."
    board["subboard_8"] = "........."
    board["subboard_9"] = "........."
    first_player_type = sys.argv[1].upper()
    second_player_type = sys.argv[2].upper()
    play_x_move(board, None, first_player_type, second_player_type)

start_game()

# Important Notes
# move = (subboard, position)