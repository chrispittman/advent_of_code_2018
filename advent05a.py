import sys
import re

input = [line.rstrip() for line in sys.stdin.readlines()]
input = input[0]
oldinput = ""

search_pattern = ''
for letter in 'qwertyuiopasdfghjklzxcvbnm':
   search_pattern += letter + letter.upper() + "|" + letter.upper() + letter + "|"
search_pattern = search_pattern[:-1]
print search_pattern

while oldinput != input:
     oldinput = input
     input = re.sub(search_pattern,'',input)
     print input

print len(input)
