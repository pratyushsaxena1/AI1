#Imports

from time import perf_counter
import sys
from collections import deque

#Create variable for the file with all possible words, create variable for the file with puzzles to solve, 
#start the timer, create a dictionary for the words and their neighbors, and create a constant for the alphabet

dictionary_file, puzzles_file, start_time, possible_words, alphabet = sys.argv[1], sys.argv[2], perf_counter(), dict(), "abcdefghijklmnopqrstuvwxyz"

#Read all possible words and add a key:value pair to the dictionary "possible_words", 
#the keys being every word and the value being a set of all its neighbors

with open(dictionary_file) as f:
    for line in f:
        word = line.strip()
        possible_words[word] = set()
        for i in range(len(word)):
            for letter in alphabet:
                neighbor = word[:i] + letter + word[i + 1:]
                if neighbor != word and neighbor in possible_words:
                    possible_words[word].add(neighbor)

#End the timer and print the relevant information; this is the end of creating the data structure to back all the words

end_time = perf_counter()
print("Time to create the data structure:", end_time - start_time, "seconds")
print("There are", len(possible_words), "words in this dict.\n")

#Start the timer and make a set of all the possible words

start_time, words_set = perf_counter(), set(possible_words)

#Generate a set of neighbors based on a given word and return the set

def generate_neighbors(word):
    neighbors = set()
    for i in range(len(word)):
        for letter in alphabet:
            neighbor = word[:i] + letter + word[i + 1:]
            if neighbor != word and neighbor in words_set:
                neighbors.add(neighbor)
    return neighbors

#Read through the puzzles to solve; use BFS algorithm principles

with open(puzzles_file) as f:
    for line_num, line in enumerate(f):
        word1, word2 = line.strip().split()
        visited = set()
        queue = deque([(word1, [word1])])
        visited.add(word1)
        while queue:
            word, ladder = queue.popleft()
            if word == word2:
                print(f"Line: {line_num}\nLength is: {len(ladder)}")
                for word_in_ladder in ladder:
                    print(word_in_ladder)
                print()
                break
            neighbors = generate_neighbors(word)
            for child in neighbors:
                if child not in visited:
                    visited.add(child)
                    queue.append((child, ladder + [child]))
        else:
            print(f"Line: {line_num}\nNo solution!\n")

#End the timer and print the relevant information; this is the end of solving the puzzles

end_time = perf_counter()
print("Time to solve all of these puzzles was:", end_time - start_time, "seconds")


#Start another timer for the brainteasers

start_time = perf_counter()

#Brainteaser 1

singleton_count = 0
for word in possible_words:
    if len(generate_neighbors(word)) == 0:
        singleton_count += 1
print("1) There are", singleton_count, "singletons.")

#Brainteaser 2

def get_component_size(word, visited):
    queue = deque([word])
    component_size = 0
    while queue:
        current_word = queue.popleft()
        if not visited[current_word]:
            visited[current_word] = True
            component_size += 1
            neighbors = generate_neighbors(current_word)
            for neighbor in neighbors:
                if not visited[neighbor]:
                    queue.append(neighbor)
    return component_size

def find_largest(possible_words):
    visited = {}
    for word in possible_words:
        visited[word] = False
    largest_size = 0
    for word in possible_words:
        if not visited[word]:
            component_size = get_component_size(word, visited)
            largest_size = max(largest_size, component_size)
    return largest_size

largest = find_largest(possible_words)
print("2) The biggest subcomponent has", largest, "words.")

#Brainteaser 3

def get_component_size(word, visited):
    queue = deque([word])
    component_size = 0
    connected_words = set()
    while queue:
        current_word = queue.popleft()
        if not visited[current_word]:
            visited[current_word] = True
            component_size += 1
            connected_words.add(current_word)
            neighbors = generate_neighbors(current_word)
            for neighbor in neighbors:
                if not visited[neighbor]:
                    queue.append(neighbor)
    return component_size, connected_words

def find_connected_subcomponents(possible_words):
    visited = {}
    for word in possible_words:
        visited[word] = False
    connected_components = []
    for word in possible_words:
        if not visited[word]:
            component_size, connected_words = get_component_size(word, visited)
            if component_size > 1:
                connected_components.append(connected_words)
    return connected_components

connected_subcomponents = find_connected_subcomponents(possible_words)
num_clumps = len(connected_subcomponents)
print("3) There are", num_clumps, "'clumps' (subgraphs with at least two words).")

#Brainteaser 4

from collections import deque

def find_longest_path(possible_words):
  max_len, max_path = 0, deque()
  visited = set()
  for word in possible_words:
    path_queue = deque([(word, deque([word]))]) 
    visited.clear()
    while path_queue:
      word, path = path_queue.popleft()  
      if len(path) > max_len:
        max_path = path
        max_len = len(path)
      for neighbor in neighbors[word]:
        if neighbor not in visited:
          visited.add(neighbor)
          new_path = path.copy()
          new_path.appendleft(neighbor)
          path_queue.append((neighbor, new_path))
  end_time = perf_counter()
  return [max_path, max_len, end_time - start_time]

neighbors = {}
for word in possible_words:
    neighbors[word] = generate_neighbors(word)
longest_path, path_length, execution_time = find_longest_path(possible_words)
print(f"4) The longest path is: [{longest_path[0]}, {longest_path[-1]}], {path_length}, found in {execution_time} seconds.")
print("The solution to this puzzle is:") 
print("Length is:", path_length)
for word in longest_path:
  print(word)