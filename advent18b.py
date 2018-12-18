import sys

input = [' '+line.rstrip()+' ' for line in sys.stdin.readlines()]
input = [' '*len(input[0])] + input + [' '*len(input[0])]
input = map(lambda s:list(s), input)

def copy_2d(a):
    return [list(a2) for a2 in a]

def update(old_board,x,y):
    if old_board[x][y]==' ':
        return ' '
    num_tree_neighbors,num_yard_neighbors = 0,0
    for x2 in [x-1,x,x+1]:
        for y2 in [y-1,y,y+1]:
            if x==x2 and y==y2:
                continue
            neighbor = old_board[x2][y2]
            if neighbor=='|': num_tree_neighbors+=1
            if neighbor=='#': num_yard_neighbors+=1
    if old_board[x][y]=='.':
        if num_tree_neighbors >= 3:
            return '|'
        else:
            return '.'
    if old_board[x][y]=='|':
        if num_yard_neighbors >= 3:
            return '#'
        else:
            return '|'
    if old_board[x][y]=='#':
        if num_tree_neighbors >= 1 and num_yard_neighbors >= 1:
            return '#'
        else:
            return '.'

    return old_board[x][y]

def count_c(board, chr):
     c = 0
     for y in range(len(board)):
         for x in range(len(board[0])):
             if board[x][y]==chr:
                 c+=1
     return c

def display(board):
    for i in range(len(board)):
        print ''.join(board[i])

# the cellular automata here settles into a cycle pretty quick -
# no need to run the whole thing
total_turns = 1
for turn in range(total_turns):
#    display(input)
    new_board = copy_2d(input)
    for x in range(1,len(input)-1):
        for y in range(1,len(input[0])-1):
            new_board[x][y] = update(input,x,y)
    input = new_board
    print turn,count_c(input,"#") * count_c(input,"|")
#display(input)

# from manual inspection of the results - when did the cycle start, and start again?
cycle_begin_turn = 9971
cycle_next_begin_turn = 9999

cycle_time = cycle_next_begin_turn - cycle_begin_turn
modulo_target = 1000000000 % cycle_time

for i in range(cycle_begin_turn,cycle_next_begin_turn):
    if i % cycle_time == modulo_target:
        print "what was the answer on turn ",(i-1),"?  That's your answer."

