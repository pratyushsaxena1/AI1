import sys

file_name = sys.argv[1]
puzzles = []

# Read in file and add to puzzles

with open(file_name) as file:
    for puzzle in file:
        puzzles.append(puzzle.strip()) 

# Define the values of the puzzle based on input

def get_puzzle_information(puzzle):
    global N, subblock_height, subblock_width, symbol_set
    N = int(len(puzzle) ** 0.5)
    factors = [i for i in range(1, N + 1) if N % i == 0]
    closest_factor = factors[0]
    min_difference = abs(N ** 0.5 - closest_factor)
    for factor in factors[1:]:
        difference = abs(N ** 0.5 - factor)
        if difference < min_difference:
            closest_factor = factor
            min_difference = difference
    subblock_width = closest_factor
    subblock_height = N // subblock_width
    symbols = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbol_set = symbols[:N]
    return N, subblock_height, subblock_width, symbol_set

# Display the puzzle

def display_puzzle(board_state, N, subblock_width, subblock_height):
    for i in range(N):
        for j in range(N):
            index = i * N + j
            print(board_state[index], end=' ')
            # Checks if end at subblock but not at end of row
            if (j + 1) % subblock_width == 0 and j + 1 != N:
                print('|', end=' ')
        print()
        # Checks if end at subblock but not at end of the entire puzzle
        if (i + 1) % subblock_height == 0 and i + 1 != N:
            print('-' * (2 * N + subblock_height))

# Make dictionary with constraints for each square

def generate_constraints(N, subblock_width, subblock_height):
    constraint_dictionary = dict()
    for square in range(N * N):
        # Row constraints
        row_start = (square // N) * N
        row_indices = set(range(row_start, row_start + N))
        row_indices.remove(square)
        # Column constraints
        column_start = square % N
        column_indices = set(range(column_start, N * N, N))
        column_indices.remove(square)
        # Block constraints
        block_indices = []
        cols_per_block = N // subblock_width
        start_row = (square // cols_per_block) * subblock_height
        start_col = (square % cols_per_block) * subblock_width
        for i in range(subblock_height):
            for j in range(subblock_width):
                row = start_row + i
                col = start_col + j
                if row * N + col != square:
                    block_indices.append(row * N + col)
        all_constraints = row_indices.union(column_indices.union(block_indices))
        constraint_dictionary[square] = all_constraints
    print(constraint_dictionary)
    return constraint_dictionary

# Count how many of each symbol there are to have a crude way to check if the solution is right- don't know if I'm supposed to implement somewhere?

def count_symbols(puzzle_grid, symbol_set):
    symbol_count = {symbol: 0 for symbol in symbol_set}
    for row in puzzle_grid:
        for symbol in row:
            if symbol in symbol_count:
                symbol_count[symbol] += 1
    for symbol, count in symbol_count.items():
        print(f"{symbol}: {count}")

# Backtracking

def is_valid(puzzle_grid, symbol, position, neighbors):
    row, col = position
    N = len(puzzle_grid)
    if symbol in puzzle_grid[row]:
        return False
    if symbol in [puzzle_grid[i][col] for i in range(N)]:
        return False
    subblock_row, subblock_col = row // subblock_height, col // subblock_width
    subblock_start_row, subblock_start_col = subblock_row * subblock_height, subblock_col * subblock_width
    subblock = [puzzle_grid[i][subblock_start_col:subblock_start_col + subblock_width] for i in range(subblock_start_row, subblock_start_row + subblock_height)]
    if symbol in [cell for row in subblock for cell in row]:
        return False
    return True

def find_empty_position(puzzle_grid):
    for i in range(len(puzzle_grid)):
        for j in range(len(puzzle_grid[0])):
            if puzzle_grid[i][j] == '.':
                return i, j
    return None

def get_sorted_values(puzzle_grid, row, col, symbol_set, neighbors):
    possible_values = [symbol for symbol in symbol_set if is_valid(puzzle_grid, symbol, (row, col), neighbors)]
    return sorted(possible_values)

def solve_sudoku(puzzle_grid, symbol_set, neighbors):
    empty_position = find_empty_position(puzzle_grid)
    if empty_position is None:
        return puzzle_grid
    row, col = empty_position
    possible_values = get_sorted_values(puzzle_grid, row, col, symbol_set, neighbors)
    for value in possible_values:
        puzzle_grid[row][col] = value
        result = solve_sudoku(puzzle_grid, symbol_set, neighbors)
        if result is not None:
            return result
        puzzle_grid[row][col] = '.'
    return None

# Find the solutions for all the puzzles

for puzzle in puzzles:
    N, subblock_width, subblock_height, symbol_set = get_puzzle_information(puzzle)
    neighbors = generate_constraints(N, subblock_width, subblock_height)
    puzzle_grid = [list(puzzle[i:i + N]) for i in range(0, N * N, N)]
    solution = solve_sudoku(puzzle_grid, symbol_set, neighbors)
    solution = ''.join([''.join(row) for row in solution])
    if solution is not None:
        print(solution)
        #display_puzzle(solution, N, subblock_width, subblock_height)
        #print()
        #count_symbols(solution, symbol_set)
    else:
        print("No solution found.")