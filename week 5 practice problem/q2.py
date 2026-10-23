def find_duplicate_team(team_names):
    for i in range(len(team_names)):
        for j in range(i + 1, len(team_names)):
            if team_names[i] == team_names[j]:
                return "Duplicate Found: " + team_names[i]

    return "No Duplicates Found"


team_names = ["ByteForce", "CodeCrafters", "ByteForce"]
print(find_duplicate_team(team_names))