from time import perf_counter
from collections import deque
import sys

def print_puzzle(board_size, string_representation):
    for i in range(board_size):
        for j in range(board_size):
            index = i * board_size + j
            character = string_representation[index]
            print(character, end=" ")
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

def bidirectional_BFS(start_node, goal_node):
    visited_start_dict = {start_node: 0}
    visited_goal_dict = {goal_node: 0}
    fringe_start = deque([(start_node, [start_node])])
    fringe_goal = deque([(goal_node, [goal_node])])
    while fringe_start and fringe_goal:
        current_state_start, path_start = fringe_start.popleft()
        current_state_goal, path_goal = fringe_goal.popleft()
        visited_start_dict[current_state_start] = len(path_start) - 1
        visited_goal_dict[current_state_goal] = len(path_goal) - 1
        common_nodes = set(visited_start_dict.keys()) & set(visited_goal_dict.keys())
        if common_nodes:
            common_node = min(common_nodes, key = lambda x: visited_start_dict[x] + visited_goal_dict[x])
            return visited_start_dict[common_node] + visited_goal_dict[common_node]
        children_start = get_children(current_state_start)
        children_goal = get_children(current_state_goal)
        for child in children_start:
            if child not in visited_start_dict:
                fringe_start.append((child, path_start + [child]))  
        for child in children_goal:
            if child not in visited_goal_dict:
                fringe_goal.append((child, path_goal + [child]))
    return None

file = sys.argv[1]
puzzles = []
with open(file) as f:
    for line in f:
        board_size, string_representation = line.strip().split()
        puzzles.append((int(board_size), string_representation))

for i, puzzle in enumerate(puzzles):
    board_size, string_representation = puzzle

    start_time_bfs = perf_counter()
    path_bfs = BFS(string_representation)
    end_time_bfs = perf_counter()

    start_time_bidirectional_bfs = perf_counter()
    path_bidirectional_bfs = bidirectional_BFS(string_representation, find_goal(string_representation))
    end_time_bidirectional_bfs = perf_counter()

    if path_bfs is None:
        print(f"Line {i}: {string_representation}, BFS: No solution found")
    else:
        num_moves_bfs = len(path_bfs)
        print(f"Line {i}: {string_representation}, BFS: {num_moves_bfs} moves found in {end_time_bfs - start_time_bfs} seconds")
    
    if path_bidirectional_bfs is None:
        print(f"Line {i}: {string_representation}, Bidirectional BFS: No solution found")
    else:
        print(f"Line {i}: {string_representation}, Bidirectional BFS: {path_bidirectional_bfs} moves found in {end_time_bidirectional_bfs - start_time_bidirectional_bfs} seconds")