import sys
from collections import deque

start_hole_index = int(sys.argv[1])
possible_moves = [(0,1,3),
                      (0,2,5),
                      (1,3,6),
                      (1,4,8),
                      (2,4,7),
                      (2,5,9),
                      (3,1,0),
                      (3,4,5),
                      (3,6,10),
                      (3,7,12),
                      (4,7,11),
                      (4,8,13),
                      (5,4,3),
                      (5,8,12),
                      (5,9,14),
                      (6,3,1),
                      (6,7,8),
                      (7,4,2),
                      (7,8,9),
                      (8,4,1),
                      (8,7,6),
                      (9,5,2),
                      (9,8,7),
                      (10,6,3),
                      (10,11,12),
                      (11,7,4),
                      (11,12,13),
                      (12,7,3),
                      (12,8,5),
                      (12,11,10),
                      (12,13,14),
                      (13,8,4),
                      (13,12,11),
                      (14,9,5),
                      (14,13,12)]
board_string = ["X" if i != start_hole_index else "." for i in range(15)]

def print_board(string_representation):
    print("    " + string_representation[0])
    print("   " + string_representation[1] + " " + string_representation[2]) 
    print("  " + string_representation[3] + " " + string_representation[4] + " " + string_representation[5])
    print(" " + string_representation[6] + " " + string_representation[7] + " " + string_representation[8] + " " + string_representation[9])
    print(string_representation[10] + " " + string_representation[11] + " " + string_representation[12] + " " + string_representation[13] + " " + string_representation[14])

def get_children(string_representation):
    children = []
    for move in possible_moves:
        a, b, c = move
        string_rep = string_representation[:]
        move_rep = string_rep[a] + string_rep[b] + string_rep[c]
        if move_rep == "XX.":
            string_rep[a] = "."
            string_rep[b] = "."
            string_rep[c] = "X"
            children.append(string_rep)
        elif move_rep == ".XX":
            string_rep[a] = "X"
            string_rep[b] = "."
            string_rep[c] = "."
            children.append(string_rep)
    return children

def goal_state(board):
    x_count = 0
    for value in board:
        if value == "X":
            x_count += 1
    if x_count == 1:
        if board[start_hole_index] == "X":
            return True
    return False

def solve_bfs(string_representation):
    queue = deque([(string_representation, [string_representation])])
    visited = set()
    while queue:
        board, path = queue.popleft()
        if goal_state(board):
            return path
        for child in get_children(board):
            if tuple(child) not in visited:
                queue.append((child, path + [child]))
                visited.add(tuple(child))

def solve_dfs(string_representation):
    stack = [(string_representation, [string_representation])]
    visited = set()
    while stack:
        board, path = stack.pop()
        if goal_state(board):
            return path
        for child in get_children(board):
            if tuple(child) not in visited:
                stack.append((child, path + [child]))
                visited.add(tuple(child))

bfs_solution = solve_bfs(board_string)
print('BFS solution:')
print("\n")
if bfs_solution:
    for board_state in bfs_solution:
        print_board(board_state)
        print("\n")
else:
    print("No solution found.")

dfs_solution = solve_dfs(board_string)
print('DFS solution:')
print("\n")
if dfs_solution:
    for board_state in dfs_solution:
        print_board(board_state)
        print("\n")
else:
    print("No solution found.")