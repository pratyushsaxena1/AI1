'''

import sys
from heapq import heappop, heappush, heapify

def parity_check(puzzle):
    puzzle_size = int(puzzle[0])
    puzzle_to_solve = puzzle[2:]
    len_unordered_pairs = len(get_unordered_pairs(puzzle_to_solve))
    blank_row = get_row(puzzle_to_solve, puzzle_size, ".")
    if puzzle_size % 2 == 1:
        return len_unordered_pairs % 2 == 0
    else:
        if blank_row % 2 == 0:
            return len_unordered_pairs % 2 == 1
        else:
            return len_unordered_pairs % 2 == 0

def get_unordered_pairs(puzzle):
    unordered_pairs_list = []
    final_puzzle = puzzle.replace(".", "").strip()
    for i, character in enumerate(final_puzzle):
        for j in range(0, i):
            if character < final_puzzle[j]:
                unordered_pairs_list.append(str(character) + (str(final_puzzle[j])))
    return unordered_pairs_list

def get_row(puzzle, puzzle_size, character_to_find):
    row_count = -1
    for i, character in enumerate(puzzle):
        if i % puzzle_size == 0:
            row_count += 1
        if character == character_to_find:
            return row_count

def find_taxicab_distance(puzzle, puzzle_size):
    puzzle = puzzle.strip()
    goal_dictionary = get_goal_dictionary(puzzle, puzzle_size)
    distance = 0
    for i in range(len(puzzle)):
        character = puzzle[i]
        if not puzzle[i] == ".":
            x, y = goal_dictionary[character]
            column_distance = abs(x - i // puzzle_size)
            row_distance = abs(y - i % puzzle_size)
            distance += column_distance + row_distance
    return distance

def get_goal_dictionary(puzzle, puzzle_size):
    board_without_period = puzzle.replace(".", "")
    sorted_string = "".join(sorted(board_without_period))
    goal_dictionary = {}
    for i, char in enumerate(sorted_string):
        goal_dictionary[char] = divmod(i, puzzle_size)
    return goal_dictionary

def get_children(board):
    board_size = int(len(board) ** 0.5)
    index_of_space = board.index('.')
    possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    children_list = []
    for x_coord, y_coord in possible_directions:
        x, y = divmod(index_of_space, board_size)
        new_x, new_y = x + x_coord, y + y_coord
        if 0 <= new_x < board_size and 0 <= new_y < board_size:
            new_index = new_x * board_size + new_y
            new_board = list(board)
            new_board[index_of_space], new_board[new_index] = new_board[new_index], new_board[index_of_space]
            children_list.append("".join(new_board))
    return children_list

def find_goal(board):
    board_without_period = board.replace(".", "")
    sorted_string = "".join(sorted(board_without_period))
    goal_state = sorted_string + "."
    return goal_state

def ASearch(board, puzzle_size):
    checked = set()
    checked.add(board)
    totDist = find_taxicab_distance(board, puzzle_size)
    fringe = [(totDist, board, 0)]
    heapify(fringe)
    while len(fringe) > 0:
        dist, state, moves = heappop(fringe)
        if board == find_goal(state):
            return moves
        for tup in get_children(state):
            heuristic, child = tup
            if child not in checked:
                heappush(fringe, (dist + heuristic + 1, child, moves + 1))
                checked.add(child)
    return None

file_name = sys.argv[1]

with open(file_name) as file:
    for i, line in enumerate(file):
        print(f"Line {i}: {ASearch(line, 4)}")

'''