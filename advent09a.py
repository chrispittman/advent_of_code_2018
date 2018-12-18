num_players = 418
last_marble_score = 70769

current_ix = 0
circle = [0]
marble_value = 0
player_scores = [0]*num_players
player_ix = -1

for i in range(last_marble_score):
    player_ix += 1
    if player_ix >= num_players:
       player_ix = 0
    marble_value += 1
    current_ix += 2
    while current_ix>len(circle):
        current_ix -= len(circle)
    if marble_value % 23 == 0:
        removed_marble_ix = current_ix - 9
        if removed_marble_ix < 0:
            removed_marble_ix += len(circle)
        removed_marble = circle[removed_marble_ix]
        score_add = marble_value + removed_marble
        circle = circle[0:removed_marble_ix] + circle[removed_marble_ix+1:]
        player_scores[player_ix] += score_add
        current_ix = removed_marble_ix
    else:
        circle = circle[0:current_ix] + [marble_value] + circle[current_ix:]

print max(player_scores)
