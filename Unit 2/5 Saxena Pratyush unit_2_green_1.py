from time import perf_counter
import random
import sys

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

def get_next_unassigned_var(state):
    for row, column in enumerate(state):
        if column is None:
            return row
    return None

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def get_sorted_values(state, var):
    n = len(state)
    legal_values = [col for col in range(n) if is_safe(state, var, col)]
    random.shuffle(legal_values)
    return legal_values

def csp_backtracking(board, row, n):
    if row == n:
        print("Solution found:", board)
        print("Test solution:", test_solution(board))
        return test_solution(board)
    var = get_next_unassigned_var(board)
    if var is None:
        return False
    for val in get_sorted_values(board, var):
        board[var] = val
        if csp_backtracking(board, row + 1, n):
            return True
        board[var] = None
    return False

def solve_n_queens(n):
    board = [None] * n
    csp_backtracking(board, 0, n)

start = perf_counter()
solve_n_queens(31)
solve_n_queens(32)
end = perf_counter()
print(end - start)