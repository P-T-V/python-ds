scores = [54, 67, 48, 99, 27]

for i_player in enumerate(scores):
    print(i_player)
print()

for i_player, i_score in enumerate(scores):
    i_score += 10
    i_player += 10
    print(i_player, i_score)
print(scores)
print()

for i_player, i_score in enumerate(scores):
    scores[i_player] += 10
    print(i_player, i_score)
print(scores)
