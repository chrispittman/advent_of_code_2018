from collections import deque

num_players = 418
last_marble_score = 7076900

#current_ix = 0
circle = deque()
circle.append(0)
marble_value = 0
player_scores = [0]*num_players
player_ix = -1

for i in range(last_marble_score):
    player_ix += 1
    if player_ix >= num_players:
       player_ix = 0
    marble_value += 1
    if marble_value % 23 == 0:
        circle.rotate(7)
        removed_marble = circle.popleft()
        score_add = marble_value + removed_marble
        player_scores[player_ix] += score_add
    else:
        circle.rotate(-2)
        circle.appendleft(marble_value)

print max(player_scores)
