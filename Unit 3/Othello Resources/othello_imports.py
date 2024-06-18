directions = [-11, -10, -9, -1, 1, 9, 10, 11]

def possible_moves(board, token):
    possible_moves, tokens = [], ["x", "o"]
    tokens.remove(token)
    enemy_token = tokens[0]
    for i, space in enumerate(board):
        if space == '.':
            for dir in directions:
                if board[i + dir] == enemy_token:
                    element = board[i + dir]
                    index = i + dir
                    while element == enemy_token:
                        index += dir
                        element = board[index]
                    if board[index] == token and i not in possible_moves:
                        possible_moves.append(i)
    return possible_moves

def make_move(board, token, index):
    board_list = list(board)
    board_list[index] = token
    for dir in directions:
        ind = index + dir
        tokens_to_flip = []
        while 0 <= ind < len(board_list) and board_list[ind] != '.' and board_list[ind] != '?' and board_list[ind] != token:
            tokens_to_flip.append(ind)
            ind += dir
        if 0 <= ind < len(board_list) and board_list[ind] == token:
            for i in tokens_to_flip:
                board_list[i] = token
    return "".join(board_list)