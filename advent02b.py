import sys
from collections import Counter

input = [line.rstrip() for line in sys.stdin.readlines()]
def search(input):
    for word1 in input:
        for word2 in input:
            num_diffs = 0
            last_diff_posn = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    num_diffs += 1
                    last_diff_posn = i
            if num_diffs == 1:
                return word1[0:last_diff_posn] + word1[last_diff_posn+1:]
    raise Exception("word not found!")
    
print search(input)
