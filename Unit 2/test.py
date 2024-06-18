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

# Display the puzzle

def display_puzzle(board_state):
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

# Make dictionary with constraints for each square; 

def generate_constraints():
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
    return constraint_dictionary

# Count how many of each symbol there are to have a crude way to check if the solution is right- don't know if I'm supposed to implement somewhere?

def count_symbols(puzzle_grid):
    symbol_count = {symbol: 0 for symbol in symbol_set}
    for row in puzzle_grid:
        for symbol in row:
            if symbol in symbol_count:
                symbol_count[symbol] += 1
    for symbol, count in symbol_count.items():
        print(f"{symbol}: {count}")

# Backtracking

def is_valid(puzzle_grid, symbol, position):
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

def get_sorted_values(puzzle_grid, row, col):
    possible_values = [symbol for symbol in symbol_set if is_valid(puzzle_grid, symbol, (row, col))]
    return sorted(possible_values)

def solve_sudoku(puzzle_grid, neighbors):
    empty_position = find_empty_position(puzzle_grid)
    if empty_position is None:
        return puzzle_grid
    row, col = empty_position
    possible_values = get_sorted_values(puzzle_grid, row, col)
    for value in possible_values:
        puzzle_grid[row][col] = value
        result = solve_sudoku(puzzle_grid, neighbors)
        if result is not None:
            return result
        puzzle_grid[row][col] = '.'
    return None

# Constraint propagation

def constraint_propagation():
    constraints = generate_constraints()
    for index, square in enumerate(puzzle):
        print(square, constraints[index])
    return puzzle

# Find the solutions for all the puzzles

for puzzle in puzzles:
    get_puzzle_information(puzzle)
    puzzle = constraint_propagation()
    neighbors = generate_constraints()
    puzzle_grid = [list(puzzle[i:i + N]) for i in range(0, N * N, N)]
    solution = solve_sudoku(puzzle_grid, neighbors)
    solution = ''.join([''.join(row) for row in solution])
    if solution is not None:
        #print(solution)
        display_puzzle(solution)
        print()
        count_symbols(solution)
    else:
        print("No solution found.")

'''

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

# Constraint propagation

def constraint_propagation(puzzle):
    constraints = generate_constraints(puzzle)
    print(constraints)
    return puzzle

# Find the solutions for all the puzzles

for puzzle in puzzles:
    puzzle = constraint_propagation(puzzle)
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

'''

'''

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

# Constraint propagation
def constraint_propagation(state, constraints):
    changes_made = True

    while changes_made:
        changes_made = False

        for box in range(N):
            box_indices = constraints[box]
            objects = [state[index] for index in box_indices]
            for symbol in symbol_set:
                if symbol not in objects:
                    present = [symbol in constraints[index] for index in box_indices]
                    if present.count(True) == 0:
                        return None, None
                    if present.count(True) == 1:
                        index = box_indices[present.index(True)]
                        state = state[:index] + symbol + state[index + 1:]
                        constraints[index] = []
                        changes_made = True

        for row in range(N):
            row_indices = constraints[N + row]
            objects = [state[index] for index in row_indices]
            for symbol in symbol_set:
                if symbol not in objects:
                    present = [symbol in constraints[index] for index in row_indices]
                    if present.count(True) == 0:
                        return None, None
                    if present.count(True) == 1:
                        index = row_indices[present.index(True)]
                        state = state[:index] + symbol + state[index + 1:]
                        constraints[index] = []
                        changes_made = True

        for col in range(N):
            col_indices = constraints[2 * N + col]
            objects = [state[index] for index in col_indices]
            for symbol in symbol_set:
                if symbol not in objects:
                    present = [symbol in constraints[index] for index in col_indices]
                    if present.count(True) == 0:
                        return None, None
                    if present.count(True) == 1:
                        index = col_indices[present.index(True)]
                        state = state[:index] + symbol + state[index + 1:]
                        constraints[index] = []
                        changes_made = True

    return state, constraints

# Find the solutions for all the puzzles
for puzzle in puzzles:
    N, subblock_width, subblock_height, symbol_set = get_puzzle_information(puzzle)
    neighbors = generate_constraints(N, subblock_width, subblock_height)
    puzzle_grid = [list(puzzle[i:i + N]) for i in range(0, N * N, N)]
    puzzle, neighbors = constraint_propagation(''.join([''.join(row) for row in puzzle_grid]), neighbors)

    while True:
        puzzle, neighbors = constraint_propagation(puzzle, neighbors)
        if puzzle is None:
            print("No solution found.")
            break

        puzzle_grid = [list(puzzle[i:i + N]) for i in range(0, N * N, N)]
        solution = solve_sudoku(puzzle_grid, symbol_set, neighbors)
        solution = ''.join([''.join(row) for row in solution])

        if solution is not None:
            print(solution)
        else:
            print("No solution found.")
            break

'''



'''

import sys
from time import perf_counter

file_name = sys.argv[1]

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

def make_constraints(board):
    N = int(len(board) ** 0.5)
    symbols = "123456789ABCDEFGHIJKLMNOPQRSTUVQXYZ"[:N]
    symbol_set = set(symbols) - {"."}
    height = -1
    i = int(N ** 0.5)
    while i < N and height == -1:
        if N % i == 0:
            height = i
        i += 1
    width = N // height

    indToBox, boxToInd = {}, {}
    box = -1
    for x in range(height * width):
        if x % height != 0:
            box -= height
        for y in range(height * width):
            ind = x * height * width + y
            if y % width == 0:
                box += 1
            indToBox[ind] = box
            lis = boxToInd.get(box, [])
            boxToInd[box] = lis + [ind]
    return N, height, width, symbol_set, indToBox, boxToInd

def is_valid(state, ind, symbol, N, indToBox, boxToInd):
    row = ind // N
    col = ind % N
    box = indToBox[ind]
    for r in range(N):
        indy = r * N + col
        if state[indy] == symbol:
            return False
        indl = row * N + r
        if state[indl] == symbol:
            return False
    for index in boxToInd[box]:
        if state[index] == symbol:
            return False
    return True

def get_next_unassigned_variable(state, possible, ones, N):
    if len(ones) > 0:
        return ones.pop()
    minNum = 10
    minInd = -1
    for index in range(N ** 2):
        if 0 < len(possible[index]) < minNum:
            minNum = len(possible[index])
            minInd = index
    return minInd

def print_board(board):
    N = int(len(board) ** 0.5)
    subblock_height = int(N ** 0.5)
    subblock_width = N // subblock_height

    for row in range(N):
        if row % subblock_height == 0:
            print()
        for split in range(subblock_height):
            left = N * row + split * subblock_width
            right = N * row + (split + 1) * subblock_width
            print(" ".join(board[left:right]), end="   ")
        print()

def populate(board):
    N = int(len(board) ** 0.5)
    symbol_set = set("123456789ABCDEFGHIJKLMNOPQRSTUVQXYZ"[:N])
    options = []
    ones = set()

    for index in range(len(board)):
        ad = ""
        if board[index] == ".":
            ad = "".join([symbol for symbol in symbol_set if is_valid(board, index, symbol, N, indToBox, boxToInd)])
            if len(ad) == 1:
                ones.add(index)
        options.append(ad)
    return options, ones

def constraint_propagation(state, dict, N, indToBox, boxToInd):
    for box in range(N):
        objects = [state[index] for index in boxToInd[box]]
        for symbol in symbol_set:
            if symbol not in objects:
                present = [symbol in dict[index] for index in boxToInd[box]]
                if present.count(True) == 0:
                    return None, None
                if present.count(True) == 1:
                    index = boxToInd[box][present.index(True)]
                    state = state[:index] + symbol + state[index + 1:]
                    dict[index] = ""
    for row in range(N):
        objects = [state[index] for index in range(N * row, N * (row + 1))]
        for symbol in symbol_set:
            if symbol not in objects:
                present = [symbol in dict[index] for index in range(N * row, N * row + N)]
                if present.count(True) == 0:
                    return None, None
                if present.count(True) == 1:
                    index = row * N + present.index(True)
                    state = state[:index] + symbol + state[index + 1:]
                    dict[index] = ""
    for col in range(N):
        for row in range(N):
            objects = [state[index] for index in range(col, N ** 2 + col, N)]
            for symbol in symbol_set:
                if symbol not in objects:
                    present = [symbol in dict[index] for index in range(col, N ** 2 + col, N)]
                    if present.count(True) == 0:
                        return None, None
                    if present.count(True) == 1:
                        index = col + N * present.index(True)
                        state = state[:index] + symbol + state[index + 1:]
                        dict[index] = ""
    return state, dict

def csp_backtracking2(state, dict, ones, N, indToBox, boxToInd):
    if "." not in state:
        return state
    if len(ones) == 0:
        state, dict = constraint_propagation(state, dict, N, indToBox, boxToInd)
        if dict is None:
            return None
        if "." not in state:
            return state

    index = get_next_unassigned_variable(state, dict, ones, N)
    for symbol in dict[index]:
        new_state = state[:index] + symbol + state[index + 1:]
        new_dict = dict.copy()
        new_dict[index] = ""
        new_dict, new_ones = forward_look(state, new_dict, index, symbol, ones.copy(), N, indToBox, boxToInd)
        if new_dict is not None:
            result = csp_backtracking2(new_state, new_dict, new_ones, N, indToBox, boxToInd)
            if result is not None:
                return result
    return None

def forward_look(state, mdict, index, symbol, ones, N, indToBox, boxToInd):
    mdict[index] = ""
    box = indToBox[index]
    for ind in boxToInd[box]:
        a = mdict[ind]
        if symbol in a:
            a = a.replace(symbol, "")
            if len(a) == 1:
                ones.add(ind)
            if len(a) == 0:
                return None, None
            mdict[ind] = a
    row = index // N
    for ind in range(N * row, N * (row + 1)):
        a = mdict[ind]
        if symbol in a:
            a = a.replace(symbol, "")
            if len(a) == 1:
                ones.add(ind)
            if len(a) == 0:
                return None, None
            mdict[ind] = a
    col = index % N
    for ind in range(col, N * N + col, N):
        a = mdict[ind]
        if symbol in a:
            a = a.replace(symbol, "")
            if len(a) == 1:
                ones.add(ind)
            if len(a) == 0:
                return None, None
            mdict[ind] = a
    return mdict, ones

def crude_check(board, symbol_set):
    if board is None:
        return False
    counts = set()
    for item in symbol_set:
        counts.add(board.count(item))
    return len(counts) == 1

def check(board, N, boxToInd):
    for box in range(N):
        myset = set()
        count = 0
        for i in boxToInd[box]:
            if board[i] == ".":
                count += 1
            else:
                myset.add(board[i])
        if len(myset) + count < N:
            return False
    for row in range(N):
        myset = set()
        count = 0
        for i in range(N * row, N * (row + 1)):
            if board[i] == ".":
                count += 1
            else:
                myset.add(board[i])
        if len(myset) + count < N:
            return False
    for col in range(N):
        myset = set()
        count = 0
        for i in range(col, N ** 2 + col, N):
            if board[i] == ".":
                count += 1
            else:
                myset.add(board[i])
        if len(myset) + count < N:
            return False
    return True

start_time = perf_counter()

boardList = []
with open(file_name) as f:
    boardList = [line.strip() for line in f]

count = 1
for board in boardList:
    N, subblock_height, subblock_width, symbol_set, indToBox, boxToInd = make_constraints(board)
    if check(board, N, boxToInd):
        dict, ones = populate(board)
        result = csp_backtracking2(board, dict, ones, N, indToBox, boxToInd)
        display_puzzle(result, N, subblock_width, subblock_height)
        print(f"{count} {crude_check(result, symbol_set)}")
    else:
        print(board)
    count += 1

end_time = perf_counter()

print(end_time - start_time)

'''

'''

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

# Display the puzzle

def display_puzzle(board_state):
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

# Make dictionary with constraints for each square; 

def generate_constraints():
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
                if row * N + col == square:
                    block_indices.append(row * N + col)
        all_constraints = row_indices.union(column_indices.union(block_indices))
        constraint_dictionary[square] = all_constraints
    return constraint_dictionary


# Count how many of each symbol there are to have a crude way to check if the solution is right- don't know if I'm supposed to implement somewhere?

def count_symbols(puzzle_grid):
    symbol_count = {symbol: 0 for symbol in symbol_set}
    for row in puzzle_grid:
        for symbol in row:
            if symbol in symbol_count:
                symbol_count[symbol] += 1
    for symbol, count in symbol_count.items():
        print(f"{symbol}: {count}")

# Backtracking

def is_valid(puzzle_grid, symbol, position):
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

def get_sorted_values(puzzle_grid, row, col):
    possible_values = [symbol for symbol in symbol_set if is_valid(puzzle_grid, symbol, (row, col))]
    return sorted(possible_values)

def solve_sudoku(puzzle_grid, neighbors):
    empty_position = find_empty_position(puzzle_grid)
    if empty_position is None:
        return puzzle_grid
    row, col = empty_position
    possible_values = get_sorted_values(puzzle_grid, row, col)
    for value in possible_values:
        puzzle_grid[row][col] = value
        result = solve_sudoku(puzzle_grid, neighbors)
        if result is not None:
            return result
        puzzle_grid[row][col] = '.'
    return None

# Constraint propagation

def constraint_propagation():
    constraints = generate_constraints()
    for index, square in enumerate(puzzle):
        row, col = index // N, index % N
        possible_values = get_sorted_values([list(puzzle[i:i + N]) for i in range(0, N * N, N)], row, col)
    return puzzle

# Find the solutions for all the puzzles

for puzzle in puzzles:
    get_puzzle_information(puzzle)
    puzzle = constraint_propagation()
    neighbors = generate_constraints()
    puzzle_grid = [list(puzzle[i:i + N]) for i in range(0, N * N, N)]
    solution = solve_sudoku(puzzle_grid, neighbors)
    solution = ''.join([''.join(row) for row in solution])
    if solution is not None:
        #print(solution)
        display_puzzle(solution)
        print()
        count_symbols(solution)
    else:
        print("No solution found.")

'''