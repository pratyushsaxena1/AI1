import sys
from time import perf_counter
from collections import deque
file_name = sys.argv[1]

cube_dict = dict()
cube_dict['Top'], cube_dict['Bottom'], cube_dict['North'], cube_dict['South'], cube_dict['East'], cube_dict['West'], cube_dict["CurrentBottom"] = ".", ".", ".", ".", ".", ".", "Bottom"

def make_2d(state):
    size = int(len(state)**0.5)
    two_d = [[0]*size for i in range(size)]
    counter = 0
    for j in range(size):
        for k in range(size):
            two_d[j][k] = state[counter]
            counter += 1
    return two_d

def swap(lst, a, b, side):
    chars = list(lst)
    print(b)
    print(chars)
    if side == "left":
        cube_dict["Top"], cube_dict["West"] = cube_dict["West"], cube_dict["Bottom"] 
        if (cube_dict["Bottom"] == "@" or chars[b] == "@") and not(cube_dict["Bottom"] == "@" and chars[b] == "@"):
            temp = chars[b]
            chars[b] = cube_dict["Bottom"]
            cube_dict["Bottom"] = temp
    if side == "right":
        cube_dict["Top"], cube_dict["East"] = cube_dict["East"], cube_dict["Bottom"] 
        if (cube_dict["Bottom"] == "@" or chars[b] == "@") and not(cube_dict["Bottom"] == "@" and chars[b] == "@"):
            temp = chars[b]
            chars[b] = cube_dict["Bottom"]
            cube_dict["Bottom"] = temp
    if side == "up":
        cube_dict["Top"], cube_dict["North"] = cube_dict["North"], cube_dict["Bottom"] 
        if (cube_dict["Bottom"] == "@" or chars[b] == "@") and not(cube_dict["Bottom"] == "@" and chars[b] == "@"):
            temp = chars[b]
            chars[b] = cube_dict["Bottom"]
            cube_dict["Bottom"] = temp
    if side == "down":
        cube_dict["Top"], cube_dict["South"] = cube_dict["South"], cube_dict["Bottom"] 
        if (cube_dict["Bottom"] == "@" or chars[b] == "@") and not(cube_dict["Bottom"] == "@" and chars[b] == "@"):
            temp = chars[b]
            chars[b] = cube_dict["Bottom"]
            cube_dict["Bottom"] = temp
    return "".join(chars) 

def get_children(board, cube_index):
    children = []
    index = 0
    size = int(len(board) ** 0.5)
    for row in range(len(board) - 1):
        index = 0
        for col in range(len(board) - 1): 
            index += 1
            if index == cube_index:
                if col > 0:
                    swap_result = make_2d(swap(board, index, index-1, "left"))
                    children.append(swap_result)
                if col < size-1:
                    swap_result = make_2d(swap(board, index, index+1, "right"))
                    children.append(swap_result)
                if row > 0:
                    swap_result = make_2d(swap(board, index, index-size, "down"))
                    children.append(swap_result)
                if row < size-1:
                    swap_result = make_2d(swap(board, index, index+size, "up"))
                    children.append(swap_result)
    return children

def goal_test(board):
    for array in board:
        if "@" in array:
            return False
    return True

def BFS_solution(board, cube_index):
    queue = deque([(board, [board])])
    visited = set()
    while queue:
        board, path = queue.popleft()
        if goal_test(board):
            return path
        for child in get_children(board, cube_index):
            if tuple(child) not in visited:
                queue.append((child, path + [child]))
                visited.add(tuple(child))

def solve_puzzle(line, cube_index):
    board_array = make_2d(line)
    return BFS_solution(board_array, cube_index)

print(get_children("....@.........................@..............@............@................@.........@..............", 40))
print(solve_puzzle("....@.........................@..............@............@................@.........@..............", 40))

# with open(file_name) as file:
#     for i, line in enumerate(file):
#         puzzle_size = int(line[0])
#         puzzle_end = (puzzle_size ** 2) + 2
#         cube_index = line[puzzle_end + 1]
#         line = line[2:puzzle_end].strip()
#         start_time = perf_counter()
#         solution = solve_puzzle(line, cube_index)
#         end_time = perf_counter()
#         # if solution is None:
#         #     print(f"Line {i}: {line}, no solution determined in {end_time - start_time} seconds")
#         # else:
#         #     print(f"Line {i}: {line}, A* - {solution} moves in {end_time - start_time} seconds")