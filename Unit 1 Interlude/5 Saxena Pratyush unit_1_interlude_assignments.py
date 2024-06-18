from time import perf_counter
import sys

sys.setrecursionlimit(5000)
problem_number, file_name, start_timer = int(sys.argv[1]), sys.argv[2], perf_counter()

#Problem 1

if problem_number == 1:
    def max_candies(prices, money):
        n = len(prices)
        table = [[0] * (money + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(money + 1):
                table[i][j] = table[i - 1][j]
                if j >= i:
                    table[i][j] = max(table[i][j], prices[i - 1] + table[i][j - i])
        return table[n][money]

    with open(file_name) as file:
        prices_dict = {i: list(map(int, line.strip().split())) for i, line in enumerate(file)}

    for key in prices_dict:
        candies = max_candies(prices_dict[key], len(prices_dict[key]))
        print(f"Max candies for day {key + 1}: {candies}")

#Problem 2

elif problem_number == 2:
    def candy_jar_game_recursive(arr):
        memo = {}
        return candy_jar_game_recursive_helper(arr, 0, memo)
    
    def candy_jar_game_recursive_helper(arr, i, memo):
        n = len(arr)
        if i >= n:
            return 0
        if i in memo:
            return memo[i]
        pick_individually = max(0, arr[i]) + candy_jar_game_recursive_helper(arr, i + 1, memo)
        pick_as_pair = 0
        if i + 1 < n:
            pick_as_pair = arr[i] * arr[i + 1] + candy_jar_game_recursive_helper(arr, i + 2, memo)
        result = max(pick_individually, pick_as_pair)
        memo[i] = result
        return result

    with open(file_name) as file:
        jar_rows_list = [list(map(int, line.strip().split())) for line in file]

    for case in jar_rows_list:
        result = candy_jar_game_recursive(case)
        print(f"Best outcome: {result}")

#Problem 3

elif problem_number == 3:
    def lcs_sequence(s1, s2):
        m, n = len(s1), len(s2)
        memo = [[[] for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    memo[i][j] = []
                elif s1[i - 1] == s2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + [s1[i - 1]]
                else:
                    memo[i][j] = memo[i - 1][j] if len(memo[i - 1][j]) > len(memo[i][j - 1]) else memo[i][j - 1]
        return memo[m][n]

    with open(file_name) as file:
        for line in file:
            s1, s2 = map(lambda x: list(map(int, x.split(','))), line.strip().split())
            sequence = lcs_sequence(s1, s2)
            print(f"LCS Sequence: {sequence}")

#Problem 4

elif problem_number == 4:
    def largest_increasing_subsequence(sequence):
        n = len(sequence)
        lis_lengths = [1] * n
        lis_sequences = [[num] for num in sequence]
        for i in range(1, n):
            for j in range(i):
                if sequence[i] > sequence[j] and lis_lengths[i] < lis_lengths[j] + 1:
                    lis_lengths[i] = lis_lengths[j] + 1
                    lis_sequences[i] = lis_sequences[j] + [sequence[i]]
        max_length_index = lis_lengths.index(max(lis_lengths))
        lis_length = lis_lengths[max_length_index]
        lis_sequence = lis_sequences[max_length_index]
        return lis_length, lis_sequence

    with open(file_name) as file:
        for line in file:
            sequence = list(map(int, line.strip().split()))
            length, lis_sequence = largest_increasing_subsequence(sequence)
            print(f"LIS Sequence: {lis_sequence}")
            print("\n")

#Problem 5

elif problem_number == 5:
    def largest_decreasing_subsequence(group_size, sequence):
        n = len(sequence)
        lis_lengths = [1] * n
        lis_sequences = [[num] for num in sequence]
        last_selected_group = [i // group_size for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if sequence[i] < sequence[j] and lis_lengths[i] <= lis_lengths[j] and last_selected_group[i] == last_selected_group[j] + 1:
                    lis_lengths[i] = lis_lengths[j] + 1
                    lis_sequences[i] = lis_sequences[j] + [sequence[i]]
                    last_selected_group[i] = i // group_size
        max_length_index = lis_lengths.index(max(lis_lengths))
        lis_sequence = lis_sequences[max_length_index]
        return lis_sequence

    with open(file_name) as file:
        for line in file:
            parts = line.strip().split()
            group_size = int(parts[0][1:-1])
            sequence = list(map(int, parts[1:]))
            result = largest_decreasing_subsequence(group_size, sequence)
            print(f"Largest Decreasing Subsequence: {result}")

#Problem 6

elif problem_number == 6:
    def best_parenthesization(numbers):
        list_values, expression_values, numbers_length = [], [], len(numbers)
        for i in range(numbers_length):
            list_values.append([0] * numbers_length)
            expression_values.append([""] * numbers_length)
        for i in range(numbers_length):
            list_values[i][i] = numbers[i]
            expression_values[i][i] = str(numbers[i])
        min_value_list = [row[:] for row in list_values]
        min_expressions_list = [row[:] for row in expression_values]
        max_value_list = [row[:] for row in list_values]
        max_expressions_list = [row[:] for row in expression_values]
        for len_value in range(1, numbers_length):
            for start_index in range(numbers_length - len_value):
                end_index = start_index + len_value
                min_value_list[start_index][end_index] = float('inf')
                max_value_list[start_index][end_index] = float('-inf')
                for index in range(start_index, end_index):
                    possibilities = [(min_value_list[start_index][index] * min_value_list[index + 1][end_index], f"({min_expressions_list[start_index][index]} * {min_expressions_list[index + 1][end_index]})"), (min_value_list[start_index][index] + min_value_list[index + 1][end_index], f"({min_expressions_list[start_index][index]} + {min_expressions_list[index + 1][end_index]})"), (min_value_list[start_index][index] * max_value_list[index + 1][end_index], f"({min_expressions_list[start_index][index]} * {max_expressions_list[index + 1][end_index]})"), (min_value_list[start_index][index] + max_value_list[index + 1][end_index], f"({min_expressions_list[start_index][index]} + {max_expressions_list[index + 1][end_index]})"), (max_value_list[start_index][index] * min_value_list[index + 1][end_index], f"({max_expressions_list[start_index][index]} * {min_expressions_list[index + 1][end_index]})"), (max_value_list[start_index][index] + min_value_list[index + 1][end_index], f"({max_expressions_list[start_index][index]} + {min_expressions_list[index + 1][end_index]})"), (max_value_list[start_index][index] * max_value_list[index + 1][end_index], f"({max_expressions_list[start_index][index]} * {max_expressions_list[index + 1][end_index]})"), (max_value_list[start_index][index] + max_value_list[index + 1][end_index], f"({max_expressions_list[start_index][index]} + {max_expressions_list[index + 1][end_index]})")]
                    for result, expression in possibilities:
                        if min_value_list[start_index][end_index] > result:
                            min_expressions_list[start_index][end_index] = expression
                            min_value_list[start_index][end_index] = result
                        if max_value_list[start_index][end_index] < result:
                            max_expressions_list[start_index][end_index] = expression
                            max_value_list[start_index][end_index] = result
        return max_value_list[0][numbers_length - 1], max_expressions_list[0][numbers_length - 1]

    with open(file_name) as file:
        parenthesization_rows_list = [list(map(int, line.strip().split())) for line in file]

    for case in parenthesization_rows_list:
        result, parenthesization = best_parenthesization(case)
        print(f"Best Parenthesization: {parenthesization} = {result}\n")

#Problem 7

elif problem_number == 7:
    print("unsolved")

#Problem 8

elif problem_number == 8:
    print("unsolved")

end_timer = perf_counter()
print(f"Execution time: {end_timer - start_timer} seconds")