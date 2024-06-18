from itertools import permutations
from collections import deque

def is_solvable(puzzle):
    puzzle = tuple(puzzle)
    inversions = 0

    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j] and puzzle[i] != 0 and puzzle[j] != 0:
                inversions += 1

    return inversions % 2 == 0

def generate_goal_state(board_size):
    return ''.join(map(str, range(1, board_size * board_size))) + '0'

def get_children(board):
    board_size = int(len(board) ** 0.5)
    index_of_space = board.index('0')
    possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    children_list = []

    for x_coord, y_coord in possible_directions:
        x, y = divmod(index_of_space, board_size)
        new_x, new_y = x + x_coord, y + y_coord

        if 0 <= new_x < board_size and 0 <= new_y < board_size:
            new_index = new_x * board_size + new_y
            new_board = list(board)
            new_board[index_of_space], new_board[new_index] = new_board[new_index], new_board[index_of_space]
            children_list.append(''.join(new_board))

    return children_list

def BFS_minimal_path(start_node):
    goal_state = generate_goal_state(3)
    visited = set()
    queue = deque([(start_node, 0, [])])  # Include path length and path in the queue
    maximal_path_length = 0
    maximal_paths = []

    while queue:
        current_state, path_length, path = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)

        if path_length > maximal_path_length:
            maximal_path_length = path_length
            maximal_paths = [(current_state, path_length, path)]
        elif path_length == maximal_path_length:
            maximal_paths.append((current_state, path_length, path))

        children = get_children(current_state)
        for child in children:
            if child not in visited:
                queue.append((child, path_length + 1, path + [child]))

    return maximal_paths

maximal_paths = BFS_minimal_path('123456780')
print(f"The 'hardest' 3x3 puzzle(s) requiring {maximal_paths[0][1]} moves:")
for start_state, path_length, path in maximal_paths:
    print(f"Start State: {start_state}")
    print(f"Solution Length: {path_length}")
    print("Solution Path:")
    for step in path:
        print(step)
    print("=" * 50)