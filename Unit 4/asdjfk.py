def grade_board(board, possible_move_index, token):
    score = 0

    #If overall game is won, add really large value
    overall_winner = get_winner(board)
    if overall_winner == token:
        score += 1000000000000000000000000000

    # Check how many subboard wins
    key_list_x = []
    key_list_o = []
    for key in board:
        winner = get_subboard_winner(board[key])
        if winner == 1:
            key_list_x.append(key)
        elif winner == -1:
            key_list_o.append(key)
    score += len(key_list_x) * 30
    score -= len(key_list_o) * 30

    # Check if important subboards are taken
    # Center
    if "subboard_5" in key_list_x:
        score += 40
    elif "subboard_5" in key_list_o:
        score -= 40
    # Corners
    if "subboard_1" in key_list_x:
        score += 20
    elif "subboard_1" in key_list_o:
        score -= 20
    if "subboard_3" in key_list_x:
        score += 20
    elif "subboard_3" in key_list_o:
        score -= 20
    if "subboard_7" in key_list_x:
        score += 20
    elif "subboard_7" in key_list_o:
        score -= 20
    if "subboard_9" in key_list_x:
        score += 20
    elif "subboard_9" in key_list_o:
        score -= 20

    # Two in a row
    if ("subboard_1" in key_list_x and "subboard_2" in key_list_x) or ("subboard_2" in key_list_x and "subboard_3" in key_list_x) or ("subboard_1" in key_list_x and "subboard_3" in key_list_x):
        score += 25
    elif ("subboard_1" in key_list_o and "subboard_2" in key_list_o) or ("subboard_2" in key_list_o and "subboard_3" in key_list_o) or ("subboard_1" in key_list_o and "subboard_3" in key_list_o):
        score -= 25
    if ("subboard_4" in key_list_x and "subboard_5" in key_list_x) or ("subboard_5" in key_list_x and "subboard_6" in key_list_x) or ("subboard_4" in key_list_x and "subboard_6" in key_list_x):
        score += 25
    elif ("subboard_4" in key_list_o and "subboard_5" in key_list_o) or ("subboard_5" in key_list_o and "subboard_6" in key_list_o) or ("subboard_4" in key_list_o and "subboard_6" in key_list_o):
        score -= 25
    if ("subboard_7" in key_list_x and "subboard_8" in key_list_x) or ("subboard_8" in key_list_x and "subboard_9" in key_list_x) or ("subboard_7" in key_list_x and "subboard_9" in key_list_x):
        score += 25
    elif ("subboard_7" in key_list_o and "subboard_8" in key_list_o) or ("subboard_8" in key_list_o and "subboard_9" in key_list_o) or ("subboard_7" in key_list_o and "subboard_9" in key_list_o):
        score -= 25
    if ("subboard_1" in key_list_x and "subboard_5" in key_list_x) or ("subboard_5" in key_list_x and "subboard_9" in key_list_x) or ("subboard_1" in key_list_x and "subboard_9" in key_list_x):
        score += 25
    elif ("subboard_1" in key_list_o and "subboard_5" in key_list_o) or ("subboard_5" in key_list_o and "subboard_9" in key_list_o) or ("subboard_1" in key_list_o and "subboard_9" in key_list_o):
        score -= 25
    if ("subboard_3" in key_list_x and "subboard_5" in key_list_x) or ("subboard_5" in key_list_x and "subboard_7" in key_list_x) or ("subboard_3" in key_list_x and "subboard_7" in key_list_x):
        score += 25
    elif ("subboard_3" in key_list_o and "subboard_5" in key_list_o) or ("subboard_5" in key_list_o and "subboard_7" in key_list_o) or ("subboard_3" in key_list_o and "subboard_7" in key_list_o):
        score -= 25

    # Two in a row with the third one open
    if ("subboard_1" in key_list_x and "subboard_2" in key_list_x and "subboard_3" not in key_list_o) or ("subboard_2" in key_list_x and "subboard_3" in key_list_x and "subboard_1" not in key_list_o) or ("subboard_1" in key_list_x and "subboard_3" in key_list_x and "subboard_2" not in key_list_o):
        score += 30
    elif ("subboard_1" in key_list_o and "subboard_2" in key_list_o and "subboard_3" not in key_list_x) or ("subboard_2" in key_list_o and "subboard_3" in key_list_o and "subboard_1" not in key_list_x) or ("subboard_1" in key_list_o and "subboard_3" in key_list_o and "subboard_2" not in key_list_x):
        score -= 30
    if ("subboard_4" in key_list_x and "subboard_5" in key_list_x and "subboard_6" not in key_list_o) or ("subboard_5" in key_list_x and "subboard_6" in key_list_x and "subboard_4" not in key_list_o) or ("subboard_4" in key_list_x and "subboard_6" in key_list_x and "subboard_5" not in key_list_o):
        score += 30
    elif ("subboard_4" in key_list_o and "subboard_5" in key_list_o and "subboard_6" not in key_list_x) or ("subboard_5" in key_list_o and "subboard_6" in key_list_o and "subboard_4" not in key_list_x) or ("subboard_4" in key_list_o and "subboard_6" in key_list_o and "subboard_5" not in key_list_x):
        score -= 30
    if ("subboard_7" in key_list_x and "subboard_8" in key_list_x and "subboard_9" not in key_list_o) or ("subboard_8" in key_list_x and "subboard_9" in key_list_x and "subboard_7" not in key_list_o) or ("subboard_7" in key_list_x and "subboard_9" in key_list_x and "subboard_8" not in key_list_o):
        score += 30
    elif ("subboard_7" in key_list_o and "subboard_8" in key_list_o and "subboard_9" not in key_list_x) or ("subboard_8" in key_list_o and "subboard_9" in key_list_o and "subboard_7" not in key_list_x) or ("subboard_7" in key_list_o and "subboard_9" in key_list_o and "subboard_8" not in key_list_x):
        score -= 30
    if ("subboard_1" in key_list_x and "subboard_5" in key_list_x and "subboard_9" not in key_list_o) or ("subboard_5" in key_list_x and "subboard_9" in key_list_x and "subboard_1" not in key_list_o) or ("subboard_1" in key_list_x and "subboard_9" in key_list_x and "subboard_5" not in key_list_o):
        score += 30
    elif ("subboard_1" in key_list_o and "subboard_5" in key_list_o and "subboard_9" not in key_list_x) or ("subboard_5" in key_list_o and "subboard_9" in key_list_o and "subboard_1" not in key_list_x) or ("subboard_1" in key_list_o and "subboard_9" in key_list_o and "subboard_5" not in key_list_x):
        score -= 30
    if ("subboard_3" in key_list_x and "subboard_5" in key_list_x and "subboard_7" not in key_list_o) or ("subboard_5" in key_list_x and "subboard_7" in key_list_x and "subboard_3" not in key_list_o) or ("subboard_3" in key_list_x and "subboard_7" in key_list_x and "subboard_5" not in key_list_o):
        score += 30
    elif ("subboard_3" in key_list_o and "subboard_5" in key_list_o and "subboard_7" not in key_list_x) or ("subboard_5" in key_list_o and "subboard_7" in key_list_o and "subboard_3" not in key_list_x) or ("subboard_3" in key_list_o and "subboard_7" in key_list_o and "subboard_5" not in key_list_x):
        score -= 30

    # Block opponent's two in a row
    if ("subboard_1" in key_list_x and "subboard_2" in key_list_x and "subboard_3" in key_list_o) or ("subboard_2" in key_list_x and "subboard_3" in key_list_x and "subboard_1" in key_list_o) or ("subboard_1" in key_list_x and "subboard_3" in key_list_x and "subboard_2" in key_list_o):
        score -= 35
    elif ("subboard_1" in key_list_o and "subboard_2" in key_list_o and "subboard_3" in key_list_x) or ("subboard_2" in key_list_o and "subboard_3" in key_list_o and "subboard_1" in key_list_x) or ("subboard_1" in key_list_o and "subboard_3" in key_list_o and "subboard_2" in key_list_x):
        score += 35
    if ("subboard_4" in key_list_x and "subboard_5" in key_list_x and "subboard_6" in key_list_o) or ("subboard_5" in key_list_x and "subboard_6" in key_list_x and "subboard_4" in key_list_o) or ("subboard_4" in key_list_x and "subboard_6" in key_list_x and "subboard_5" in key_list_o):
        score -= 35
    elif ("subboard_4" in key_list_o and "subboard_5" in key_list_o and "subboard_6" in key_list_x) or ("subboard_5" in key_list_o and "subboard_6" in key_list_o and "subboard_4" in key_list_x) or ("subboard_4" in key_list_o and "subboard_6" in key_list_o and "subboard_5" in key_list_x):
        score += 35
    if ("subboard_7" in key_list_x and "subboard_8" in key_list_x and "subboard_9" in key_list_o) or ("subboard_8" in key_list_x and "subboard_9" in key_list_x and "subboard_7" in key_list_o) or ("subboard_7" in key_list_x and "subboard_9" in key_list_x and "subboard_8" in key_list_o):
        score -= 35
    elif ("subboard_7" in key_list_o and "subboard_8" in key_list_o and "subboard_9" in key_list_x) or ("subboard_8" in key_list_o and "subboard_9" in key_list_o and "subboard_7" in key_list_x) or ("subboard_7" in key_list_o and "subboard_9" in key_list_o and "subboard_8" in key_list_x):
        score += 35
    if ("subboard_1" in key_list_x and "subboard_5" in key_list_x and "subboard_9" in key_list_o) or ("subboard_5" in key_list_x and "subboard_9" in key_list_x and "subboard_1" in key_list_o) or ("subboard_1" in key_list_x and "subboard_9" in key_list_x and "subboard_5" in key_list_o):
        score -= 35
    elif ("subboard_1" in key_list_o and "subboard_5" in key_list_o and "subboard_9" in key_list_x) or ("subboard_5" in key_list_o and "subboard_9" in key_list_o and "subboard_1" in key_list_x) or ("subboard_1" in key_list_o and "subboard_9" in key_list_o and "subboard_5" in key_list_x):
        score += 35
    if ("subboard_3" in key_list_x and "subboard_5" in key_list_x and "subboard_7" in key_list_o) or ("subboard_5" in key_list_x and "subboard_7" in key_list_x and "subboard_3" in key_list_o) or ("subboard_3" in key_list_x and "subboard_7" in key_list_x and "subboard_5" in key_list_o):
        score -= 35
    elif ("subboard_3" in key_list_o and "subboard_5" in key_list_o and "subboard_7" in key_list_x) or ("subboard_5" in key_list_o and "subboard_7" in key_list_o and "subboard_3" in key_list_x) or ("subboard_3" in key_list_o and "subboard_7" in key_list_o and "subboard_5" in key_list_x):
        score += 35
    
    # Check for good sequence within subboards
    for key in board:
        temp_board = board[key]
        # Good if you have 2 in a row
        # Check for two in a row in each row
        if temp_board[0] == temp_board[1] == 'X' or temp_board[1] == temp_board[2] == 'X' or temp_board[0] == temp_board[2] == 'X':
            score += 5
        if temp_board[3] == temp_board[4] == 'X' or temp_board[4] == temp_board[5] == 'X' or temp_board[3] == temp_board[5] == 'X':
            score += 5
        if temp_board[6] == temp_board[7] == 'X' or temp_board[7] == temp_board[8] == 'X' or temp_board[6] == temp_board[8] == 'X':
            score += 5
        if temp_board[0] == temp_board[1] == 'O' or temp_board[1] == temp_board[2] == 'O' or temp_board[0] == temp_board[2] == 'O':
            score -= 5
        if temp_board[3] == temp_board[4] == 'O' or temp_board[4] == temp_board[5] == 'O' or temp_board[3] == temp_board[5] == 'O':
            score -= 5
        if temp_board[6] == temp_board[7] == 'O' or temp_board[7] == temp_board[8] == 'O' or temp_board[6] == temp_board[8] == 'O':
            score -= 5
        # Check for two in a row in each column
        if temp_board[0] == temp_board[3] == 'X' or temp_board[3] == temp_board[6] == 'X' or temp_board[0] == temp_board[6] == 'X':
            score += 5
        if temp_board[1] == temp_board[4] == 'X' or temp_board[4] == temp_board[7] == 'X' or temp_board[1] == temp_board[7] == 'X':
            score += 5
        if temp_board[2] == temp_board[5] == 'X' or temp_board[5] == temp_board[8] == 'X' or temp_board[2] == temp_board[8] == 'X':
            score += 5
        if temp_board[0] == temp_board[3] == 'O' or temp_board[3] == temp_board[6] == 'O' or temp_board[0] == temp_board[6] == 'O':
            score -= 5
        if temp_board[1] == temp_board[4] == 'O' or temp_board[4] == temp_board[7] == 'O' or temp_board[1] == temp_board[7] == 'O':
            score -= 5
        if temp_board[2] == temp_board[5] == 'O' or temp_board[5] == temp_board[8] == 'O' or temp_board[2] == temp_board[8] == 'O':
            score -= 5
        # Check for two in a row in diagonals
        if temp_board[0] == temp_board[4] == 'X' or temp_board[4] == temp_board[8] == 'X' or temp_board[0] == temp_board[8] == 'X':
            score += 5
        if temp_board[2] == temp_board[4] == 'X' or temp_board[4] == temp_board[6] == 'X' or temp_board[2] == temp_board[6] == 'X':
            score += 5
        if temp_board[0] == temp_board[4] == 'O' or temp_board[4] == temp_board[8] == 'O' or temp_board[0] == temp_board[8] == 'O':
            score -= 5
        if temp_board[2] == temp_board[4] == 'O' or temp_board[4] == temp_board[6] == 'O' or temp_board[2] == temp_board[6] == 'O':
            score -= 5
        
        # Even better if you have 2 in a row that aren't blocked by an opponent
        # Check for two in a row without opponent blocking in each row
        if temp_board[0] == temp_board[1] == 'X' and temp_board[2] == '.' or temp_board[1] == temp_board[2] == 'X' and temp_board[0] == '.' or temp_board[0] == temp_board[2] == 'X' and temp_board[1] == '.':
            score += 10
        if temp_board[3] == temp_board[4] == 'X' and temp_board[5] == '.' or temp_board[4] == temp_board[5] == 'X' and temp_board[3] == '.' or temp_board[3] == temp_board[5] == 'X' and temp_board[4] == '.':
            score += 10
        if temp_board[6] == temp_board[7] == 'X' and temp_board[8] == '.' or temp_board[7] == temp_board[8] == 'X' and temp_board[6] == '.' or temp_board[6] == temp_board[8] == 'X' and temp_board[7] == '.':
            score += 10
        if temp_board[0] == temp_board[1] == 'O' and temp_board[2] == '.' or temp_board[1] == temp_board[2] == 'O' and temp_board[0] == '.' or temp_board[0] == temp_board[2] == 'O' and temp_board[1] == '.':
            score -= 10
        if temp_board[3] == temp_board[4] == 'O' and temp_board[5] == '.' or temp_board[4] == temp_board[5] == 'O' and temp_board[3] == '.' or temp_board[3] == temp_board[5] == 'O' and temp_board[4] == '.':
            score -= 10
        if temp_board[6] == temp_board[7] == 'O' and temp_board[8] == '.' or temp_board[7] == temp_board[8] == 'O' and temp_board[6] == '.' or temp_board[6] == temp_board[8] == 'O' and temp_board[7] == '.':
            score -= 10
        # Check for two in a row without opponent blocking in each column
        if temp_board[0] == temp_board[3] == 'X' and temp_board[6] == '.' or temp_board[3] == temp_board[6] == 'X' and temp_board[0] == '.' or temp_board[0] == temp_board[6] == 'X' and temp_board[3] == '.':
            score += 10
        if temp_board[1] == temp_board[4] == 'X' and temp_board[7] == '.' or temp_board[4] == temp_board[7] == 'X' and temp_board[1] == '.' or temp_board[1] == temp_board[7] == 'X' and temp_board[4] == '.':
            score += 10
        if temp_board[2] == temp_board[5] == 'X' and temp_board[8] == '.' or temp_board[5] == temp_board[8] == 'X' and temp_board[2] == '.' or temp_board[2] == temp_board[8] == 'X' and temp_board[5] == '.':
            score += 10
        if temp_board[0] == temp_board[3] == 'O' and temp_board[6] == '.' or temp_board[3] == temp_board[6] == 'O' and temp_board[0] == '.' or temp_board[0] == temp_board[6] == 'O' and temp_board[3] == '.':
            score -= 10
        if temp_board[1] == temp_board[4] == 'O' and temp_board[7] == '.' or temp_board[4] == temp_board[7] == 'O' and temp_board[1] == '.' or temp_board[1] == temp_board[7] == 'O' and temp_board[4] == '.':
            score -= 10
        if temp_board[2] == temp_board[5] == 'O' and temp_board[8] == '.' or temp_board[5] == temp_board[8] == 'O' and temp_board[2] == '.' or temp_board[2] == temp_board[8] == 'O' and temp_board[5] == '.':
            score -= 10
        # Check for two in a row without opponent blocking in diagonals
        if temp_board[0] == temp_board[4] == 'X' and temp_board[8] == '.' or temp_board[4] == temp_board[8] == 'X' and temp_board[0] == '.' or temp_board[0] == temp_board[8] == 'X' and temp_board[4] == '.':
            score += 10
        if temp_board[2] == temp_board[4] == 'X' and temp_board[6] == '.' or temp_board[4] == temp_board[6] == 'X' and temp_board[2] == '.' or temp_board[2] == temp_board[6] == 'X' and temp_board[4] == '.':
            score += 10
        if temp_board[0] == temp_board[4] == 'O' and temp_board[8] == '.' or temp_board[4] == temp_board[8] == 'O' and temp_board[0] == '.' or temp_board[0] == temp_board[8] == 'O' and temp_board[4] == '.':
            score -= 10
        if temp_board[2] == temp_board[4] == 'O' and temp_board[6] == '.' or temp_board[4] == temp_board[6] == 'O' and temp_board[2] == '.' or temp_board[2] == temp_board[6] == 'O' and temp_board[4] == '.':
            score -= 10

        # Good if you block opponent's 2 in a row
        # Check if opponent's two in a row is blocked (rows)
        if (temp_board[0] == temp_board[1] == 'O' and temp_board[2] == 'X') or (temp_board[1] == temp_board[2] == 'O' and temp_board[0] == 'X') or (temp_board[0] == temp_board[2] == 'O' and temp_board[1] == 'X'):
            score += 15
        elif (temp_board[0] == temp_board[1] == 'X' and temp_board[2] == 'O') or (temp_board[1] == temp_board[2] == 'X' and temp_board[0] == 'O') or (temp_board[0] == temp_board[2] == 'X' and temp_board[1] == 'O'):
            score -= 15
        if (temp_board[3] == temp_board[4] == 'O' and temp_board[5] == 'X') or (temp_board[4] == temp_board[5] == 'O' and temp_board[3] == 'X') or (temp_board[3] == temp_board[5] == 'O' and temp_board[4] == 'X'):
            score += 15
        elif (temp_board[3] == temp_board[4] == 'X' and temp_board[5] == 'O') or (temp_board[4] == temp_board[5] == 'X' and temp_board[3] == 'O') or (temp_board[3] == temp_board[5] == 'X' and temp_board[4] == 'O'):
            score -= 15
        if (temp_board[6] == temp_board[7] == 'O' and temp_board[8] == 'X') or (temp_board[7] == temp_board[8] == 'O' and temp_board[6] == 'X') or (temp_board[6] == temp_board[8] == 'O' and temp_board[7] == 'X'):
            score += 15
        elif (temp_board[6] == temp_board[7] == 'X' and temp_board[8] == 'O') or (temp_board[7] == temp_board[8] == 'X' and temp_board[6] == 'O') or (temp_board[6] == temp_board[8] == 'X' and temp_board[7] == 'O'):
            score -= 15
        # Check if opponent's two in a row is blocked (columns)
        if (temp_board[0] == temp_board[3] == 'O' and temp_board[6] == 'X') or (temp_board[3] == temp_board[6] == 'O' and temp_board[0] == 'X') or (temp_board[0] == temp_board[6] == 'O' and temp_board[3] == 'X'):
            score += 15
        elif (temp_board[0] == temp_board[3] == 'X' and temp_board[6] == 'O') or (temp_board[3] == temp_board[6] == 'X' and temp_board[0] == 'O') or (temp_board[0] == temp_board[6] == 'X' and temp_board[3] == 'O'):
            score -= 15
        if (temp_board[1] == temp_board[4] == 'O' and temp_board[7] == 'X') or (temp_board[4] == temp_board[7] == 'O' and temp_board[1] == 'X') or (temp_board[1] == temp_board[7] == 'O' and temp_board[4] == 'X'):
            score += 15
        elif (temp_board[1] == temp_board[4] == 'X' and temp_board[7] == 'O') or (temp_board[4] == temp_board[7] == 'X' and temp_board[1] == 'O') or (temp_board[1] == temp_board[7] == 'X' and temp_board[4] == 'O'):
            score -= 15
        if (temp_board[2] == temp_board[5] == 'O' and temp_board[8] == 'X') or (temp_board[5] == temp_board[8] == 'O' and temp_board[2] == 'X') or (temp_board[2] == temp_board[8] == 'O' and temp_board[5] == 'X'):
            score += 15
        elif (temp_board[2] == temp_board[5] == 'X' and temp_board[8] == 'O') or (temp_board[5] == temp_board[8] == 'X' and temp_board[2] == 'O') or (temp_board[2] == temp_board[5] == 'X' and temp_board[8] == 'O'):
            score -= 15
        # Check if opponent's two in a row is blocked (diagonals)
        if (temp_board[0] == temp_board[4] == 'O' and temp_board[8] == 'X') or (temp_board[4] == temp_board[8] == 'O' and temp_board[0] == 'X') or (temp_board[0] == temp_board[8] == 'O' and temp_board[4] == 'X'):
            score += 15
        elif (temp_board[0] == temp_board[4] == 'X' and temp_board[8] == 'O') or (temp_board[4] == temp_board[8] == 'X' and temp_board[0] == 'O') or (temp_board[0] == temp_board[8] == 'X' and temp_board[4] == 'O'):
            score -= 15
        if (temp_board[2] == temp_board[4] == 'O' and temp_board[6] == 'X') or (temp_board[4] == temp_board[6] == 'O' and temp_board[2] == 'X') or (temp_board[2] == temp_board[6] == 'O' and temp_board[4] == 'X'):
            score += 15
        elif (temp_board[2] == temp_board[4] == 'X' and temp_board[6] == 'O') or (temp_board[4] == temp_board[6] == 'X' and temp_board[2] == 'O') or (temp_board[2] == temp_board[4] == 'X' and temp_board[6] == 'O'):
            score -= 15

    # Don't give opponent a move where they can pick subboard too
    if get_subboard_winner(board["subboard_" + str(possible_move_index)]) is not None:
        if token == 'X':
            score -= 200
        elif token == 'O':
            score += 200

    return score