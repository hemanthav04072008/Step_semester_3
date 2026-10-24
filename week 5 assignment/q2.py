def find_duplicate_pick(player_names):
    for i in range(len(player_names)):
        for j in range(i + 1, len(player_names)):
            if player_names[i] == player_names[j]:
                return "Duplicate Found: " + player_names[i]

    return "No Duplicates Found"


player_names = ["Kohli", "Bumrah", "Kohli", "Rohit"]

print(find_duplicate_pick(player_names))