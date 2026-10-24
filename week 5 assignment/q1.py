def apply_multipliers(player_scores, captain_index, vice_captain_index):
    player_scores[captain_index] *= 2
    player_scores[vice_captain_index] *= 1.5


scores = [40.0, 55.0, 30.0, 62.0]

apply_multipliers(scores, 1, 3)

print(scores)