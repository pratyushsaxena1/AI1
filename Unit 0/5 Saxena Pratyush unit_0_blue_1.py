from time import perf_counter
start = perf_counter()
import sys
import heapq
from heapq import heappush, heappop

f1, f2, f3 = sys.argv[1], sys.argv[2], sys.argv[3]
with open(f1) as f:
    first_file_list = [int(line.strip()) for line in f]
    first_file_set = set(first_file_list)
with open(f2) as f:
    second_file_list = [int(line.strip()) for line in f]
    second_file_set = set(second_file_list)
with open(f3) as f:
    third_file_list = [int(line.strip()) for line in f]
    third_file_set = set(third_file_list)

#1
count = 0
for val in first_file_set:
    if val in second_file_set:
        count += 1
print("#1:", count)

#2
sum_vals = 0
values = set()
position = 0
for val in first_file_list:
    if val not in values:
        values.add(val)
        position += 1
        if position % 100 == 0:
            sum_vals += int(val)
print("#2:", sum_vals)

#3
count_repeats = 0
third_file_dict = {}
for val in third_file_set:
    third_file_dict[val] = 1
for val in first_file_list:
    if third_file_dict.get(val) == 1:
        count_repeats += 1
for val in second_file_list:
    if third_file_dict.get(val) == 1:
        count_repeats += 1
print("#3:", count_repeats)

#4
final_list = []
sorted_list = list(sorted(set(first_file_list)))
for i in range(10):
    final_list.append(sorted_list[i])
print("#4:", final_list)

#5
second_file_dict = {}
for val in second_file_set:
    second_file_dict[val] = 0
for val in second_file_list:
    second_file_dict[val] += 1
reverse_sorted_list = []
for key in second_file_dict.keys():
    if second_file_dict.get(key) > 1:
        reverse_sorted_list.append(key)
reverse_sorted_list = sorted(reverse_sorted_list, reverse = True)
final_reversed_list = []
for i in range(10):
    final_reversed_list.append(reverse_sorted_list[i])
print("#5:", final_reversed_list)

#6
sequence = set()
heap = []
for index, val in enumerate(first_file_list):
    heapq.heappush(heap, val)
    if val % 53 == 0:
        while heap[0] in sequence:
            heapq.heappop(heap)
        sequence.add(heap[0])
print("#6:", sum(sequence))

end = perf_counter()
print("Total time:", end - start)