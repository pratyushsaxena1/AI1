from time import perf_counter
from collections import deque
import sys

file = sys.argv[1]
puzzles = []

with open(file) as f:
    for line in f:
        string_representation = line.strip()
        puzzles.append(string_representation)

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

def goal_test(node):
    return node[0] == find_goal(node[0])

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

def ID_DFS(start_state):
    max_depth = 0
    result = None
    while result is None:
        result = k_DFS(start_state, max_depth)
        max_depth += 1
    return result

def k_DFS(start_state, k):
    fringe = []
    fringe.append((start_state, 0, {start_state}))
    while fringe:
        state, depth, ancestors = fringe.pop()
        if find_goal(state) == state:
            return state, depth, ancestors
        if depth < k:
            children = get_children(state)
            for child in children:
                if child not in ancestors:
                    temp = (child, depth + 1, ancestors | {child})
                    fringe.append(temp)
    return None


for i, puzzle in enumerate(puzzles):
    string_representation = puzzle

    start_time_bfs = perf_counter()
    path_bfs = BFS(string_representation)
    end_time_bfs = perf_counter()

    start_time_dfs = perf_counter()
    path_dfs = ID_DFS(string_representation)
    end_time_dfs = perf_counter()

    if path_bfs is None:
        print(f"Line {i}: {string_representation}, BFS - No solution found")
    else:
        num_moves_bfs = len(path_bfs)
        print(f"Line {i}: {string_representation}, BFS - {num_moves_bfs} moves in {end_time_bfs - start_time_bfs} seconds")

    if path_dfs is None:
        print(f"Line {i}: {string_representation}, ID-DFS - No solution found")
    else:
        num_moves_dfs = path_dfs[1]
        print(f"Line {i}: {string_representation}, ID-DFS - {num_moves_dfs} moves in {end_time_dfs - start_time_dfs} seconds")