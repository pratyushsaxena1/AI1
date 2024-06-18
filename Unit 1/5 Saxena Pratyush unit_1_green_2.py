from time import perf_counter
start_time = perf_counter()
import sys
from collections import deque
file = sys.argv[1]
puzzles = []
with open(file) as f:
    for line in f:
        board_size, string_representation = line.strip().split()
        puzzles.append((int(board_size), string_representation))

def print_puzzle(board_size, string_representation):
    for i in range(board_size):
        for j in range(board_size):
            index = i * board_size + j
            character = string_representation[index]
            print(character, end = " ")
        print()

def find_goal(board):
    board_without_period = board.replace(".", "")
    sorted_string = "".join(sorted(board_without_period))
    goal_state = sorted_string + "."
    return goal_state

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

def BFS(start_node):
    goal_state = find_goal(start_node)
    visited = set()
    fringe = deque([(start_node, [])])
    while fringe:
        current_state, path = fringe.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)
        if current_state == goal_state:
            return path
        children = get_children(current_state)
        for child in children:
            if child not in visited:
                fringe.append((child, path + [child]))
    return None

for i, puzzle in enumerate(puzzles):
    board_size, string_representation = puzzle
    path = BFS(string_representation)
    if path is None:
        print(f"Line {i}: {string_representation}, No solution found")
    else:
        num_moves = len(path)
        end_time = perf_counter()
        print(f"Line {i}: {string_representation}, {num_moves} moves found in {end_time - start_time} seconds")