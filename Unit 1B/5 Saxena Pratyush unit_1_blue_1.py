import sys
from time import perf_counter
from collections import deque
file_name = sys.argv[1]

cube_dict = dict()
cube_dict['Top'], cube_dict['Bottom'], cube_dict['North'], cube_dict['South'], cube_dict['East'], cube_dict['West'], cube_dict["CurrentBottom"] = ".", ".", ".", ".", ".", ".", "Bottom"

def swap(lst, a, b, side):
    chars = list(lst)
    if side == "left":
        cube_dict["Top"], cube_dict["West"] = cube_dict["West"], cube_dict["Bottom"] 
        if (cube_dict["Bottom"] == "@" or chars[b] == "@"):
            temp = chars[b]
            chars[b] = cube_dict["Bottom"]
            cube_dict["Bottom"] = temp
    if side == "right":
        cube_dict["Top"], cube_dict["East"] = cube_dict["East"], cube_dict["Bottom"] 
        if (cube_dict["Bottom"] == "@" or chars[b] == "@"):
            temp = chars[b]
            chars[b] = cube_dict["Bottom"]
            cube_dict["Bottom"] = temp
    if side == "up":
        cube_dict["Top"], cube_dict["North"] = cube_dict["North"], cube_dict["Bottom"] 
        if (cube_dict["Bottom"] == "@" or chars[b] == "@"):
            temp = chars[b]
            chars[b] = cube_dict["Bottom"]
            cube_dict["Bottom"] = temp
    if side == "down":
        cube_dict["Top"], cube_dict["South"] = cube_dict["South"], cube_dict["Bottom"] 
        if (cube_dict["Bottom"] == "@" or chars[b] == "@"):
            temp = chars[b]
            chars[b] = cube_dict["Bottom"]
            cube_dict["Bottom"] = temp
    return "".join(chars) 

def get_children(board, cube_index):
    children = []
    index = -1
    size = int(len(board) ** 0.5)
    for row in range(size):
        for col in range(size): 
            index += 1
            if index == cube_index:
                if col > 0:
                    swap_result = (swap(board, index, index - 2, "left"))
                    children.append(swap_result)
                if col < size-1:
                    swap_result = (swap(board, index, index, "right"))
                    children.append(swap_result)
                if row > 0:
                    swap_result = (swap(board, index, index-size, "down"))
                    children.append(swap_result)
                if row < size-1:
                    swap_result = (swap(board, index, index+size, "up"))
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
    return BFS_solution(line, cube_index)

with open(file_name) as file:
    for i, line in enumerate(file):
        puzzle_size = int(line[0])
        puzzle_end = (puzzle_size ** 2) + 2
        cube_index = line[puzzle_end + 1]
        line = line[2:puzzle_end].strip()
        start_time = perf_counter()
        solution = solve_puzzle(line, cube_index)
        end_time = perf_counter()
        if solution is None:
            print(f"Line {i}: {line}, no solution determined in {end_time - start_time} seconds")
        else:
            print(f"Line {i}: {line}, A* - {solution} moves in {end_time - start_time} seconds")