class Player:
    def __init__(self, name, matches_played, batting_average, injured):
        self.name = name
        self.matches_played = matches_played
        self.batting_average = batting_average
        self.injured = injured

    @staticmethod
    def is_draftable(matches_played, injured=None):
        if injured is None:
            return matches_played >= 10

        return matches_played >= 5 and not injured

    def __lt__(self, other):
        # Sort batting averages in descending order
        return self.batting_average > other.batting_average


def draft_and_rank(players):
    draftable = []

    for player in players:
        if (
            Player.is_draftable(player.matches_played)
            or Player.is_draftable(
                player.matches_played, player.injured
            )
        ):
            draftable.append(player)

    ranked = sorted(draftable)

    if not ranked:
        return "No players drafted"

    result = []

    for i, player in enumerate(ranked, start=1):
        result.append(f"{i}. {player.name}")

    return " | ".join(result)


players = [
    Player("Virat", 15, 48.0, False),
    Player("Rahul", 7, 55.0, False),
    Player("Sameer", 3, 60.0, False),
    Player("Dev", 12, 20.0, True)
]

print(draft_and_rank(players))