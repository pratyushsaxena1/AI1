from time import perf_counter
start = perf_counter()

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and i != x:
            return False
    return True

def problem_1():
    return sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0)

def problem_2():
    sum, first_num, second_num = 0, 1, 2
    while first_num < 4000000:
        if first_num % 2 == 0:
            sum += first_num
        first_num, second_num = second_num, first_num + second_num
    return sum

def problem_3():
    for i in range(int(600851475143 ** 0.5) + 1, 2, -1):
        if 600851475143 % i == 0 and is_prime(i):
            return i

def problem_4():
    for first_num in range(900, 1000):
        for second_num in range(900, 1000):
            if str(first_num * second_num) == str(first_num * second_num)[::-1]:
                max_palindrome = str(first_num * second_num)
    return max_palindrome

def problem_6():
    return sum(x for x in list(range(1, 101))) ** 2 - sum((x ** 2) for x in list(range(1, 101)))

def problem_7():
    tracker, iterator, is_done = 0, 1, False
    while not is_done:
        iterator += 1
        if is_prime(iterator):
            tracker += 1
        if tracker == 10001:
            is_done = True
    return iterator

def problem_8():
    num_string = "731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385" +\
            "861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689" +\
            "664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589" +\
            "072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333" +\
            "001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797" +\
            "784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844" +\
            "031998900088952434506585412275886668811642717147992444292823086346567481391912316282458617866458359124" +\
            "566529476545682848912883142607690042242190226710556263211111093705442175069416589604080719840385096245" +\
            "544436298123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094050" +\
            "7754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    largest_product, constant = 0, 1
    while len(num_string) != 0:
        temp_list = []
        for x in num_string[0:13]:
            temp_list.append(int(x))
        for x in temp_list:
            constant = constant * x
        if constant > largest_product:
            largest_product = constant
        num_string, constant = num_string[1:], 1
    return largest_product

def problem_9():
    for c in range(1, 1000):
        for b in range(1, 400):
            for a in range(1, 300):
                if a + b + c == 1000:
                    if ((a ** 2) + (b ** 2) == (c ** 2)):
                        return a * b * c

def problem_12():
    tracker, triangle_num, is_found = 7, 28, False
    while not is_found:
        num_of_divisors = 2
        for i in range(2, int(triangle_num**0.5) + 1):
            if triangle_num % i == 0:
                num_of_divisors += 2
        if num_of_divisors > 500:
            is_found = True
        else:
            tracker += 1
            triangle_num += tracker
    return triangle_num

def problem_14():
    tracker, max_chain_num, max_num, current_num, current_chain_num = 0, 0, 0, 0, 0
    for i in range(1000000, 1, -1):
        current_num, tracker = i, i
        while tracker != 1:
            if tracker % 2 == 0:
                tracker = tracker / 2
            else:
                tracker = (tracker * 3) + 1
            current_chain_num += 1
        if current_chain_num > max_chain_num:
                max_chain_num, max_num = current_chain_num, current_num
        current_chain_num = 0
    return max_num

def problem_18():
    data = [[75],
       [95, 64],
       [17, 47, 82],
       [18, 35, 87, 10],
       [20,  4, 82, 47, 65],
       [19,  1, 23, 75,  3, 34],
       [88,  2, 77, 73,  7, 63, 67],
       [99, 65,  4, 28,  6, 16, 70, 92],
       [41, 41, 26, 56, 83, 40, 80, 70, 33],
       [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
       [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
       [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
       [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
       [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
       [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]
    for i in range(len(data) - 2, -1, -1):
        for z in range(len(data[i])):
            data[i][z] += max(data[i + 1][z + 1], data[i + 1][z])
    return data[0][0]

def problem_24():
    num_permutation, result, digits = 999999, [], list(range(10))
    for i in range(9, 0, -1):
        factorial = 1
        for z in range(1, i + 1):
            factorial *= z
        even_divisor, num_permutation = divmod(num_permutation, factorial)
        result.append(digits.pop(even_divisor))
    result.append(digits[0])
    return ''.join([str(num) for num in result])

def problem_28():
    spiral_sum, current_number, tracker = 1, 1, 2
    for i in range(1001 // 2):
        for i in range(4):
            current_number += tracker
            spiral_sum += current_number
        tracker += 2
    return spiral_sum

def problem_29():
    return len({i ** j for i in range(2, 101) for j in range(2, 101)})


print("#1:", problem_1())
print("#2:", problem_2())
print("#3:", problem_3())
print("#4:", problem_4())
print("#6:", problem_6())
print("#7:", problem_7())
print("#8:", problem_8())
print("#9:", problem_9())
print("#12:", problem_12())
print("#14", problem_14())
print("#18", problem_18())
print("#24:", problem_24())
print("#28:", problem_28())
print("#29:", problem_29())

end = perf_counter()
print("Total time:", end - start)