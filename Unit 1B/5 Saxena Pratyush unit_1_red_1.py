import sys
import heapq
from time import perf_counter

file_name = sys.argv[1]

def parity_check(puzzle_to_solve, puzzle_size):
    len_unordered_pairs = len(get_unordered_pairs(puzzle_to_solve))
    blank_row = get_row(puzzle_to_solve, puzzle_size, ".")
    if puzzle_size % 2 == 1:
        return len_unordered_pairs % 2 == 0
    else:
        return (len_unordered_pairs % 2 == 1) == (blank_row % 2 == 0)

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

def get_goal_dictionary(puzzle, puzzle_size):
    board_without_period = puzzle.replace(".", "")
    sorted_string = "".join(sorted(board_without_period))
    goal_dictionary = {}
    for i, char in enumerate(sorted_string):
        goal_dictionary[char] = divmod(i, puzzle_size)
    return goal_dictionary

def find_taxicab_distance(puzzle, puzzle_size, goal_dict):
    puzzle = puzzle.strip()
    distance = 0
    for i in range(len(puzzle)):
        character = puzzle[i]
        if character != ".":
            x, y = goal_dict[character]
            column_distance = abs(x - i // puzzle_size)
            row_distance = abs(y - i % puzzle_size)
            distance += column_distance + row_distance
    return distance

def get_children(board, goal_dict, puzzle_size):
    board_size = int(len(board) ** 0.5)
    index_of_space = board.index('.')
    possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x_space, y_space = divmod(index_of_space, board_size)
    children_list = []
    for x_coord, y_coord in possible_directions:
        new_x, new_y = x_space + x_coord, y_space + y_coord
        if 0 <= new_x < puzzle_size and 0 <= new_y < puzzle_size:
            new_index = new_x * puzzle_size + new_y
            new_board = list(board)
            new_board[index_of_space], new_board[new_index] = new_board[new_index], new_board[index_of_space]
            children_list.append("".join(new_board))
    return children_list

def a_star(start_state, puzzle_size):
    closed = set()
    start_node = start_state
    goal_dict = get_goal_dictionary(start_state, puzzle_size)
    fringe = []
    if not parity_check(start_state, puzzle_size):
        return None
    start_distance = find_taxicab_distance(start_node, puzzle_size, goal_dict)
    heapq.heappush(fringe, (start_distance, start_node, 0))
    while fringe:
        f, s, d = heapq.heappop(fringe)
        if find_taxicab_distance(s, puzzle_size, goal_dict) == 0:
            return d
        if s not in closed:
            closed.add(s)
            for child in get_children(s, goal_dict, puzzle_size):
                if child not in closed:
                    child_distance = find_taxicab_distance(child, puzzle_size, goal_dict)
                    heapq.heappush(fringe, (child_distance + d + 1, child, d + 1))
    return None

with open(file_name) as file:
    for i, line in enumerate(file):
        start_time = perf_counter()
        solution = a_star(line.strip(), 4)
        end_time = perf_counter()
        if solution is None:
            print(f"Line {i + 1}: {line.strip()}, no solution determined in {end_time - start_time} seconds")
        else:
            print(f"Line {i + 1}: {line.strip()}, A* - {solution} moves in {end_time - start_time} seconds")