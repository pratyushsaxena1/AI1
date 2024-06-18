from time import perf_counter
import random

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

def get_conflicts_num(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def solve_n_queens(n):
    board = list(range(n))
    print(f"Initial Conflicts: {get_conflicts_num(board)} \n{board}\n")
    while True:
        conflicts, min_conflicts_queens = float('inf'), []
        for i in range(n):
            original_col = board[i]
            for j in range(n):
                if j != original_col:
                    board[i] = j
                    new_conflicts = get_conflicts_num(board)
                    if new_conflicts < conflicts:
                        conflicts, min_conflicts_queens = new_conflicts, [i]
                    elif new_conflicts == conflicts:
                        min_conflicts_queens.append(i)
            board[i] = original_col
        randomly_selected_queen = random.choice(min_conflicts_queens)
        row_attacks = [get_conflicts_num(board[:randomly_selected_queen] + [i] + board[randomly_selected_queen+1:]) for i in range(n)]
        min_attacks = min(row_attacks)
        min_attack_positions = [i for i, j in enumerate(row_attacks) if j == min_attacks]
        random_new_position = random.choice(min_attack_positions)
        board[randomly_selected_queen] = random_new_position
        print(f"Conflicts: {get_conflicts_num(board)}")
        print(f"Current Board State: {board}")
        if conflicts == 0:
            break
    print(f"\nFinal State: {board}")
    print(f"Final Conflicts: {get_conflicts_num(board)}")
    if test_solution(board):
        print("Solution is valid!\n")
    else:
        print("Solution is invalid!\n")

start = perf_counter()
solve_n_queens(31)
solve_n_queens(32)
end = perf_counter()
print("Total Time:", end - start)