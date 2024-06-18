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
    def well_spaced_largest_decreasing_subsequence(group_size, sequence):
        n = len(sequence)
        table = [None] * n
        for i in range(n):
            table[i] = [sequence[i]]
            for j in range(i):
                if sequence[i] < sequence[j] and (i - j) % group_size == 0:
                    new_subsequence = table[j] + [sequence[i]]
                    if len(new_subsequence) > len(table[i]):
                        table[i] = new_subsequence
        max_subsequence = max(table, key=len, default=[])
        return max_subsequence

    with open(file_name) as file:
        for line in file:
            parts = line.strip().split()
            group_size = int(parts[0][1:-1])
            sequence = list(map(int, parts[1:]))
            result = well_spaced_largest_decreasing_subsequence(group_size, sequence)
            print(f"Largest Decreasing Subsequence: {result}")




#Problem 6

elif problem_number == 6:
    def best_parenthesization(sequence):
        memo = {}
        result, parenthesization = best_parenthesization_recursive(sequence, 0, len(sequence) - 1, memo)
        return result, parenthesization

    def best_parenthesization_recursive(sequence, i, j, memo):
        if i == j:
            return sequence[i], str(sequence[i])
        if (i, j) in memo:
            return memo[(i, j)]
        max_result = float('-inf')
        best_expression = ""
        for k in range(i, j):
            a, expr_a = best_parenthesization_recursive(sequence, i, k, memo)
            b, expr_b = best_parenthesization_recursive(sequence, k + 1, j, memo)  
            option1 = a * b
            option2 = a + b
            if option1 > max_result:
                max_result = option1
                best_expression = f"({expr_a}) * ({expr_b})"
            if option2 > max_result:
                max_result = option2
                best_expression = f"({expr_a}) + ({expr_b})"
        memo[(i, j)] = max_result, best_expression
        return max_result, best_expression

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