import sys

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

def get_winner(game_board):
    key_list_x = []
    key_list_o = []
    for key in game_board:
        winner = get_subboard_winner(game_board[key])
        if winner == 1:
            key_list_x.append(key)
        elif winner == -1:
            key_list_o.append(key)
    if "subboard1" in key_list_x and "subboard2" in key_list_x and "subboard3" in key_list_x or "subboard4" in key_list_x and "subboard5" in key_list_x and "subboard6" in key_list_x or "subboard7" in key_list_x and "subboard8" in key_list_x and "subboard9" in key_list_x or "subboard1" in key_list_x and "subboard4" in key_list_x and "subboard7" in key_list_x or "subboard2" in key_list_x and "subboard5" in key_list_x and "subboard8" in key_list_x or "subboard3" in key_list_x and "subboard6" in key_list_x and "subboard9" in key_list_x or "subboard1" in key_list_x and "subboard5" in key_list_x and "subboard9" in key_list_x or "subboard3" in key_list_x and "subboard5" in key_list_x and "subboard7" in key_list_x:
        return "x"
    elif "subboard1" in key_list_o and "subboard2" in key_list_o and "subboard3" in key_list_o or "subboard4" in key_list_o and "subboard5" in key_list_o and "subboard6" in key_list_o or "subboard7" in key_list_o and "subboard8" in key_list_o and "subboard9" in key_list_o or "subboard1" in key_list_o and "subboard4" in key_list_o and "subboard7" in key_list_o or "subboard2" in key_list_o and "subboard5" in key_list_o and "subboard8" in key_list_o or "subboard3" in key_list_o and "subboard6" in key_list_o and "subboard9" in key_list_o or "subboard1" in key_list_o and "subboard5" in key_list_o and "subboard9" in key_list_o or "subboard3" in key_list_o and "subboard5" in key_list_o and "subboard7" in key_list_o:
        return "o"
    elif len(key_list_x) + len(key_list_o) == 9:
        return "tie"
    else:
        return "none"

def is_valid_move(board, subboard, position):
    try:
        board_key = "subboard_" + str(subboard)
        if board[board_key][position - 1] == ".":
            return True
    except:
        return False
    return False

def play_first_move(board, subboard, position, piece):
    board_key = "subboard_" + str(subboard)
    updated_board = board[board_key][:(position - 1)] + str(piece) + board[board_key][position:]
    board[board_key] = updated_board
    display_board(board)
    play_o_move(board, position)

def play_move(board, subboard, position, piece):
    board_key = "subboard_" + str(subboard)
    updated_board = board[board_key][:(position - 1)] + str(piece) + board[board_key][position:]
    board[board_key] = updated_board
    return board

def play_x_move(board, previous_move):
    if get_subboard_winner(board["subboard_" + str(previous_move)]) != None:
        move_board = int(input("Player 1, pick a board 1-9 to play a move in: "))
        move_position = int(input("Now, pick a position in that board 1-9: "))
        if is_valid_move(board, move_board, move_position):
            board = play_move(board, move_board, move_position, "X")
        else:
            print("That's an invalid move. Please try again.")
            play_x_move(board, previous_move)
    else:
        move_position = int(input("Player 1, pick a position 1-9 in board " + str(previous_move) + ": "))
        board_key = "subboard_" + str(previous_move)
        if is_valid_move(board, previous_move, move_position):
            updated_board = board[board_key][:(move_position - 1)] + "X" + board[board_key][move_position:]
            board[board_key] = updated_board
        else:
            print("That's an invalid move. Please try again.")
            play_x_move(board, previous_move)
    display_board(board)
    winner = get_winner(board)
    if winner == "x":
        print("\nCongratulations! Player 1 wins!\n")
        sys.exit()
    elif winner == "tie":
        print("\It's a tie!\n")
        sys.exit()
    play_o_move(board, move_position)

def play_o_move(board, previous_move):
    if get_subboard_winner(board["subboard_" + str(previous_move)]) != None:
        move_board = int(input("Player 2, pick a board 1-9 to play a move in: "))
        move_position = int(input("Now, pick a position in that board 1-9: "))
        if is_valid_move(board, move_board, move_position):
            board = play_move(board, move_board, move_position, "O")
        else:
            print("That's an invalid move. Please try again.")
            play_o_move(board, previous_move)
    else:
        move_position = int(input("Player 2, pick a position 1-9 in board " + str(previous_move) + ": "))
        board_key = "subboard_" + str(previous_move)
        if is_valid_move(board, previous_move, move_position):
            updated_board = board[board_key][:(move_position - 1)] + "O" + board[board_key][move_position:]
            board[board_key] = updated_board
        else:
            print("That's an invalid move. Please try again.")
            play_o_move(board, previous_move)
    display_board(board)
    winner = get_winner(board)
    if winner == "o":
        print("\nCongratulations! Player 2 wins!\n")
        sys.exit()
    elif winner == "tie":
        print("\It's a tie!\n")
        sys.exit()
    play_x_move(board, move_position)

def call_first_move(game_board):
    allowed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    first_move_board = int(input("Player 1, you are playing as X. First, pick a board 1-9 to play a move in: "))
    first_move_position = int(input("Now, pick a position in that board 1-9: "))
    if first_move_board in allowed and first_move_position in allowed:
        play_first_move(game_board, first_move_board, first_move_position, "X")
    else:
        print("That's an invalid move. Please try again.")
        call_first_move(game_board)

def start_game():
    print("This game is called Ultimate Tic Tac Toe. Essentially, it's a Tic Tac Toe game, but every square has another Tic Tac Toe grid inside it. Players attempt to win three small boards in a row to win.")
    game_board = dict()
    game_board["subboard_1"] = "........."
    game_board["subboard_2"] = "........."
    game_board["subboard_3"] = "........."
    game_board["subboard_4"] = "........."
    game_board["subboard_5"] = "........."
    game_board["subboard_6"] = "........."
    game_board["subboard_7"] = "........."
    game_board["subboard_8"] = "........."
    game_board["subboard_9"] = "........."
    display_board(game_board)
    call_first_move(game_board)

start_game()