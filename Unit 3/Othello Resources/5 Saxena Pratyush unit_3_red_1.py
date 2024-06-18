import sys
import random

directions = [-11, -10, -9, -1, 1, 9, 10, 11]

def find_next_move(board, player, depth):
    return max_move(board, depth) if player == 'x' else min_move(board, depth)
    
def max_move(board, depth):
    possible_moves = get_possible_moves(board, 'x')
    max_number, max_index = -1000000000000000, -1
    for index in possible_moves:
        current_number = min_step(make_move(board, 'x', index), -1000000000000000, 1000000000000000, depth)
        if current_number > max_number:
            max_number, max_index = current_number, index
    return max_index

def min_move(board, depth):
    possible_moves = get_possible_moves(board, 'o')
    min_number, min_index = 1000000000000000, -1
    for index in possible_moves:
        current_number = max_step(make_move(board, 'o', index), -1000000000000000, 1000000000000000, depth)
        if current_number < min_number:
            min_number, min_index = current_number, index
    return min_index

# ALPHA/BETA PRUNING HERE
def max_step(board, alpha, beta, depth):
    if depth == 0:
        return grade_board(board, 'x')
    max_number = -1000000
    for possible_board in get_possible_boards(board, 'x'):
        current_result = min_step(possible_board, alpha, beta, depth - 1)
        if current_result >= beta:
            return current_result
        if current_result > alpha:
            alpha = current_result
        max_number = max(max_number, current_result)
    return max_number

# ALPHA/BETA PRUNING HERE
def min_step(board, alpha, beta, depth):
    if depth == 0:
        return grade_board(board, 'o')
    min_number = 1000000
    for possible_board in get_possible_boards(board, 'o'):
        current_result = max_step(possible_board, alpha, beta, depth - 1)
        if alpha >= current_result:
            return current_result
        if beta > current_result:
            beta = current_result
        min_number = min(min_number, current_result)
    return min_number
        
def grade_board(board, player):
    weightage_factors = {}
    num_of_spaces = board.count('.')
    score, players = 0, ['x', 'o']
    players.remove(player)
    enemy = players[0]
    if player == 'x': #Maximize score
        if num_of_spaces > 54:
            weightage_factors['mobility'] = 100
            weightage_factors['corner'] = 0
            weightage_factors['corner_adjacent'] = 0
            weightage_factors['diagnol'] = 0
            weightage_factors['edge'] = 0
            weightage_factors['most_pieces'] = 0
        elif num_of_spaces > 50:
            weightage_factors['mobility'] = 12
            weightage_factors['corner'] = 200
            weightage_factors['corner_adjacent'] = 40
            weightage_factors['diagnol'] = 30
            weightage_factors['edge'] = 5
            weightage_factors['most_pieces'] = 0
        elif num_of_spaces > 40:
            weightage_factors['mobility'] = 10
            weightage_factors['corner'] = 200
            weightage_factors['corner_adjacent'] = 40
            weightage_factors['diagnol'] = 40
            weightage_factors['edge'] = 10
            weightage_factors['most_pieces'] = 0
        elif num_of_spaces > 30:
            weightage_factors['mobility'] = 8
            weightage_factors['corner'] = 200
            weightage_factors['corner_adjacent'] = 40
            weightage_factors['diagnol'] = 50
            weightage_factors['edge'] = 20
            weightage_factors['most_pieces'] = 0
        elif num_of_spaces > 20:
            weightage_factors['mobility'] = 6
            weightage_factors['corner'] = 200
            weightage_factors['corner_adjacent'] = 40
            weightage_factors['diagnol'] = 40
            weightage_factors['edge'] = 40
            weightage_factors['most_pieces'] = 10
        elif num_of_spaces > 10:
            weightage_factors['mobility'] = 2
            weightage_factors['corner'] = 100
            weightage_factors['corner_adjacent'] = 40
            weightage_factors['diagnol'] = 30
            weightage_factors['edge'] = 40
            weightage_factors['most_pieces'] = 40
        elif num_of_spaces > 5:
            weightage_factors['mobility'] = 2
            weightage_factors['corner'] = 100
            weightage_factors['corner_adjacent'] = 40
            weightage_factors['diagnol'] = 10
            weightage_factors['edge'] = 40
            weightage_factors['most_pieces'] = 80
        else:
            weightage_factors['mobility'] = 0
            weightage_factors['corner'] = 0
            weightage_factors['corner_adjacent'] = 0
            weightage_factors['diagnol'] = 0
            weightage_factors['edge'] = 0
            weightage_factors['most_pieces'] = 100
    else: #Minimize score
        if num_of_spaces > 54:
            weightage_factors['mobility'] = -100
            weightage_factors['corner'] = 0
            weightage_factors['corner_adjacent'] = 0
            weightage_factors['diagnol'] = 0
            weightage_factors['edge'] = 0
            weightage_factors['most_pieces'] = 0
        elif num_of_spaces > 50:
            weightage_factors['mobility'] = -12
            weightage_factors['corner'] = -200
            weightage_factors['corner_adjacent'] = -40
            weightage_factors['diagnol'] = -30
            weightage_factors['edge'] = -5
            weightage_factors['most_pieces'] = 0
        elif num_of_spaces > 40:
            weightage_factors['mobility'] = -10
            weightage_factors['corner'] = -200
            weightage_factors['corner_adjacent'] = -40
            weightage_factors['diagnol'] = -40
            weightage_factors['edge'] = -10
            weightage_factors['most_pieces'] = 0
        elif num_of_spaces > 30:
            weightage_factors['mobility'] = 8
            weightage_factors['corner'] = -200
            weightage_factors['corner_adjacent'] = -40
            weightage_factors['diagnol'] = -50
            weightage_factors['edge'] = -20
            weightage_factors['most_pieces'] = 0
        elif num_of_spaces > 20:
            weightage_factors['mobility'] = -6
            weightage_factors['corner'] = -200
            weightage_factors['corner_adjacent'] = -40
            weightage_factors['diagnol'] = -40
            weightage_factors['edge'] = -40
            weightage_factors['most_pieces'] = -10
        elif num_of_spaces > 10:
            weightage_factors['mobility'] = -2
            weightage_factors['corner'] = -100
            weightage_factors['corner_adjacent'] = -40
            weightage_factors['diagnol'] = -30
            weightage_factors['edge'] = -40
            weightage_factors['most_pieces'] = -40
        elif num_of_spaces > 5:
            weightage_factors['mobility'] = -2
            weightage_factors['corner'] = -100
            weightage_factors['corner_adjacent'] = -40
            weightage_factors['diagnol'] = -10
            weightage_factors['edge'] = -40
            weightage_factors['most_pieces'] = -80
        else:
            weightage_factors['mobility'] = 0
            weightage_factors['corner'] = 0
            weightage_factors['corner_adjacent'] = 0
            weightage_factors['diagnol'] = 0
            weightage_factors['edge'] = 0
            weightage_factors['most_pieces'] = -100
    
    # Check win
    if num_of_spaces == 0:
        if board.count(player) > board.count(enemy):
            score = 1000000000000
        else:
            score = -1000000000000
    
    # Check corners and spaces around
    corners_dict = {11: [12, 21, 22], 18: [17, 27, 28], 81: [71, 72, 82], 88: [87, 78, 77]}
    corners_gotten = []
    for corner in corners_dict:
        if board[corner] == player:
            corners_gotten.append(corner)
            score += weightage_factors['corner']
        for space in corners_dict[corner]:
            if board[space] == player:
                if board[corner] == player:
                    score += weightage_factors['corner_adjacent'] / 2
                else:
                    score -= weightage_factors['corner_adjacent']
    
    # Check diagnols
    diagnol_bottom_left_to_top_right = [34, 45, 54, 63, 72, 81]
    diagnol_top_left_to_bottom_right = [36, 45, 56, 67, 78, 89]
    if 18 in corners_gotten or 81 in corners_gotten:
        for piece in diagnol_bottom_left_to_top_right:
            if board[piece] == player:
                score += weightage_factors['diagnol']
            elif board[piece] == enemy:
                score -= weightage_factors['diagnol']

    if 11 in corners_gotten or 88 in corners_gotten:
        for piece in diagnol_top_left_to_bottom_right:
            if board[piece] == player:
                score += weightage_factors['diagnol']
            elif board[piece] == enemy:
                score -= weightage_factors['diagnol']
    
    # Check edges
    edges = [11, 13, 14, 15, 16, 18, 31, 41, 51, 61, 81, 38, 48, 58, 68, 88, 83, 84, 85, 86]
    for edge in edges:
        if board[edge] == player:
            for corner in corners_gotten:
                if abs(edge - corner) == 10:
                    score += weightage_factors['edge'] * 2
            score += weightage_factors['edge']
        if board[edge] == enemy:
            for corner in corners_gotten:
                if abs(edge - corner) == 10:
                    score -= weightage_factors['edge'] * 2
            score -= weightage_factors['edge']
    
    # For every 2 more tokens I have than other player, multiply and add to score
    score += (((board.count(player) - board.count(enemy)) / 2) * weightage_factors['most_pieces'])
    
    # For every move more, multiply by mobility
    score += (len(get_possible_boards(board, player)) - len(get_possible_boards(board, enemy))) * weightage_factors['mobility']
    
    return score

def get_possible_boards(board, player):
    return [make_move(board, player, move) for move in get_possible_moves(board, player)]

def get_possible_moves(board, token):
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
    tokens = ["x", "o"]
    tokens.remove(token)
    enemy_token = tokens[0]
    board_list = list(board)
    board_list[index] = token
    for dir in directions:
        ind = index + dir
        tokens_to_flip = []
        while 0 <= ind < len(board_list) and board_list[ind] == enemy_token:
            tokens_to_flip.append(ind)
            ind += dir
        if 0 <= ind < len(board_list) and board_list[ind] == token:
            for i in tokens_to_flip:
                board_list[i] = token
    return "".join(board_list)

class Strategy():
   logging = True
   uses_10x10_board = True
   uses_10x10_moves = True
   def best_strategy(self, board, player, best_move, still_running):
       depth = 1
       for count in range(board.count(".")):
           best_move.value = find_next_move(board, player, depth)
           depth += 1

if __name__ == "__main__":
    board = sys.argv[1]
    player = sys.argv[2]
    depth = 1
    for count in range(board.count(".")):
        print(find_next_move(board, player, depth))
        depth += 1