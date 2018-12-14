
scores = [3,7]

elf_posns = [0,1]

def round():
    sum = scores[elf_posns[0]] + scores[elf_posns[1]]
    if sum<10:
       scores.append(sum)
    else:
       scores.append(sum/10)
       scores.append(sum%10)
    elf_posns[0] += 1 + scores[elf_posns[0]]
    elf_posns[1] += 1 + scores[elf_posns[1]]
    while elf_posns[0]>=len(scores):
        elf_posns[0] -= len(scores)
    while elf_posns[1]>=len(scores):
        elf_posns[1] -= len(scores)

def score_string():
    return "".join([str(s) for s in scores])

for i in range(100000000):
    round()

search_string = "030121"
while search_string not in score_string():
    round()

print score_string().index(search_string)
