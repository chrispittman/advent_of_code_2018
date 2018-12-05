import sys
import re

input = [line.rstrip() for line in sys.stdin.readlines()]
input = input[0]

search_pattern = ''
all_letters = 'qwertyuiopasdfghjklzxcvbnm'
for letter in all_letters:
    search_pattern += letter + letter.upper() + "|" + letter.upper() + letter + "|"
search_pattern = search_pattern[:-1]

def react(input):
    oldinput = ''
    while oldinput != input:
        oldinput = input
        input = re.sub(search_pattern,'',input)
    return len(input)

lengths = []
for letter_to_remove in all_letters:
    search_input = re.sub(letter_to_remove + "|" + letter_to_remove.upper(), '', input)
    lengths.append(react(search_input))

print min(lengths)
