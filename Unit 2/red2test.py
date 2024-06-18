import sys

def get_puzzle_information(puzzle):
    global N, subblock_width, subblock_height, symbol_set
    puzzle_size = len(puzzle)
    N = int(puzzle_size ** 0.5)
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
    symbols = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbol_set = symbols[:N]
    return N, subblock_height, subblock_width, symbol_set

def display_puzzle(puzzle, N, subblock_width, subblock_height):
    for i in range(N):
        for j in range(N):
            index = i * N + j
            print(puzzle[index], end=" ")
            if (j + 1) % subblock_height == 0 and j + 1 != N:
                print("|", end=" ")
        print()
        if (i + 1) % subblock_width == 0 and i + 1 != N:
            print("-" * (2 * N + subblock_width))

def test_solution(puzzle):
    for i in puzzle:
        if i != "." and len(i) != 1:
            return False
    return True

def get_constraints(puzzle):
    current_N, current_subblock_width, current_subblock_height, _ = get_puzzle_information(puzzle)
    rows = [set(range(i * N, (i + 1) * current_N)) for i in range(current_N)]
    columns = [set(range(i, current_N ** 2, current_N)) for i in range(N)]
    blocks = []
    for i in range(0, current_N, current_subblock_width):
        for j in range(0, current_N, current_subblock_height):
            block = set()
            for x in range(current_subblock_width):
                for z in range(current_subblock_height):
                    block.add((current_N * (j + z)) + (i + x))
            blocks.append(block)
    return rows, columns, blocks

def get_neighbors(puzzle):
    rows, columns, blocks = get_constraints(puzzle)
    neighbors_dict = {}
    index_tracker = 0
    for _ in puzzle:
        final_row = next((row for row in rows if index_tracker in row), set())
        final_column = next((column for column in columns if index_tracker in column), set())
        final_block = next((block for block in blocks if index_tracker in block), set())
        neighbors = final_row.union(final_column.union(final_block))
        neighbors.remove(index_tracker)
        neighbors_dict[index_tracker] = neighbors
        index_tracker += 1
    return neighbors_dict

def assign_test_value(puzzle, variable, value):
    puzzle_copy = puzzle.copy()
    puzzle_copy[variable] = value
    return puzzle_copy

def get_most_constrained_variable(puzzle):
    max_possibilities = 1
    for i in puzzle:
        current_possibilities = len(i)
        if current_possibilities > max_possibilities:
            max_possibilities = current_possibilities
    for i in puzzle:
        current_possibilities = len(i)
        if current_possibilities == max_possibilities:
            return puzzle.index(i)

def forward_looking(puzzle, neighbors_dict):
    solved_indices = {index for index, element in enumerate(puzzle) if len(element) == 1}
    while solved_indices:
        index = solved_indices.pop()
        neighbors = neighbors_dict[index]
        neighbors.discard(index)
        for neighbor in neighbors:
            if len(puzzle[neighbor]) == 1 and puzzle[neighbor] == puzzle[index]:
                return None
            if len(puzzle[neighbor]) > 1 and puzzle[index] in puzzle[neighbor]:
                updated_set = set(puzzle[neighbor]) - {puzzle[index]}
                puzzle[neighbor] = "".join(updated_set)
                if len(puzzle[neighbor]) == 1:
                    solved_indices.add(neighbor)
                elif len(puzzle[neighbor]) == 0:
                    return None
    return puzzle

def constraint_propagation(puzzle, row, column, block):
    all_constraints = row + column + block
    for constraint in all_constraints:
        values = {}
        for element in constraint:
            if len(puzzle[element]) == 0:
                return None
            for value in puzzle[element]:
                if value not in values:
                    values[value] = [element]
                else:
                    values[value].append(element)
        for value, indices in values.items():
            if len(indices) == 1:
                puzzle[indices[0]] = value
    return puzzle

def final_sudoku_solver(puzzle, neighbors_dict, row, column, block):
    if test_solution(puzzle):
        return puzzle
    most_constrained_variable = get_most_constrained_variable(puzzle)
    for value in sorted(puzzle[most_constrained_variable]):
        checked_board = forward_looking(constraint_propagation(assign_test_value(puzzle, most_constrained_variable, value), row, column, block), neighbors_dict)
        if checked_board is not None:
            result = final_sudoku_solver(checked_board, neighbors_dict, row, column, block)
            if result is not None:
                return result
    return None

s = sys.argv[1]
with open(s) as f:
    for line in f:
        line = line.strip()
        get_puzzle_information(line)
        neighbors_dict = get_neighbors(line)
        row, column, block = get_constraints(line)
        puzzle_as_list = forward_looking([i if i != "." else "".join(str(j) for j in symbol_set) for i in line], neighbors_dict)
        solution = final_sudoku_solver(puzzle_as_list, neighbors_dict, row, column, block)
        if solution is not None:
            print("".join(solution))
        else:
            print("No solution")