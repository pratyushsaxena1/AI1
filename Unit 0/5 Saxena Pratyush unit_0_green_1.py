import sys

first_letter = sys.argv[1]

if first_letter == 'A':
    print(int(sys.argv[2]) + int(sys.argv[3]) + int(sys.argv[4]))

elif first_letter == 'B':
    sum = 0
    for arg in sys.argv[2:]:
        sum += int(arg)
    print(sum)

elif first_letter == 'C':
    list = []
    for arg in sys.argv[2:]:
        if int(arg) % 3 == 0:
            list.append(arg)
    print(list)

elif first_letter == 'D':
    list2 = []
    first_num = 1
    second_num = 1
    for i in range(int(sys.argv[2])):
        list2.append(first_num)
        temp = first_num
        first_num = second_num
        second_num = temp + second_num
    print(list2)

elif first_letter == 'E':
    list3 = []
    base_num = int(sys.argv[2])
    for i in range(int(sys.argv[3]) - int(sys.argv[2]) + 1):
        k = base_num + i
        list3.append((k ** 2) - (3 * k) + 2)
    print(list3)

elif first_letter == 'F':
    first_input = float(sys.argv[2])
    second_input = float(sys.argv[3])
    third_input = float(sys.argv[4])
    if first_input + second_input < third_input or first_input + third_input < second_input or second_input + third_input < first_input:
        print("Error: These side lengths don't make a valid triangle.")
    else:
        s = (first_input + second_input + third_input) / 2
        print((s * (s - first_input) * (s - second_input) * (s - third_input)) ** 0.5)

elif first_letter == 'G':
    my_string = sys.argv[2].lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    for char in my_string:
        if char in vowels:
            if char == 'a':
                a_count += 1
            elif char == 'e':
                e_count += 1
            elif char == 'i':
                i_count += 1
            elif char == 'o':
                o_count += 1
            elif char == 'u':
                u_count += 1
    print("a count: ", a_count)
    print("e count: ", e_count)
    print("i count: ", i_count)
    print("o count: ", o_count)
    print("u count: ", u_count)