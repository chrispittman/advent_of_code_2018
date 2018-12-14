
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

num_recipes = 30121
while len(scores) < 10+num_recipes:
    round()

# print scores
print "".join([str(s) for s in scores[num_recipes:num_recipes+10]])
