import sys

try:
    file_name, min_length, current_game = sys.argv[1], sys.argv[2], sys.argv[3]
except:
    file_name, min_length, current_game = sys.argv[1], sys.argv[2], ""

possible_words = []
with open(file_name) as file:
    for line in file:
        word = line.strip().upper()
        if word.isalpha() and len(word) >= int(min_length) and word[:len(current_game)] == current_game:
                possible_words.append(word)

def max_move(current_word, current_possible_words, alpha, beta):
    if current_word in current_possible_words:
        return 100
    possible_outcomes, next_letter = [], get_next_letter(current_word, current_possible_words)
    for letter in next_letter.keys():
        current_result = min_move(current_word + letter, next_letter[letter], alpha, beta)
        if current_result >= beta:
            return current_result
        if current_result > alpha:
            alpha = current_result
        possible_outcomes.append(current_result)
    return min(alpha, max(possible_outcomes))

def min_move(current_word, current_possible_words, alpha, beta):
    if current_word in current_possible_words:
        return -100
    possible_outcomes, next_letter = [], get_next_letter(current_word, current_possible_words)
    for letter in next_letter.keys():
        current_result = max_move(current_word + letter, next_letter[letter], alpha, beta)
        if alpha >= current_result:
            return current_result
        if beta > current_result:
            beta = current_result
        possible_outcomes.append(current_result)
    return max(alpha, min(possible_outcomes))

def get_next_letter(current_word, current_possible_words):
    possible_letters = dict()
    for word in current_possible_words:
        next_letter = word[len(current_word)]
        try:
            possible_letters[next_letter] = possible_letters.get(next_letter) + [word]
        except:
            possible_letters[next_letter] = [word]
    return possible_letters

success_letters, next_letter = [], get_next_letter(current_game, possible_words)
for letter in next_letter.keys():
    current_result = min_move(current_game + letter, next_letter[letter], -10000000000, 10000000000)
    if current_result == 100:
        success_letters.append(letter)
if len(success_letters) == 0:
    print("Next player will lose!")
else:
    print("Next player can guarantee victory by playing any of these letters:", success_letters)