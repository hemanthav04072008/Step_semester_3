import random

moves = ["Rock", "Paper", "Scissors"]
results = []
wins = losses = draws = 0

n = 5

for i in range(n):
    player = input("Enter Rock, Paper, or Scissors: ").capitalize()
    computer = random.choice(moves)

    if player not in moves:
        print("Invalid move! Try again.")
        continue

    if player == computer:
        result = "Draw"
        draws += 1
    elif ((player == "Rock" and computer == "Scissors") or
          (player == "Paper" and computer == "Rock") or
          (player == "Scissors" and computer == "Paper")):
        result = "Player Wins"
        wins += 1
    else:
        result = "Computer Wins"
        losses += 1

    results.append((i + 1, player, computer, result))
    print(result)

print("\nRound | Player | Computer | Result")
for r in results:
    print(r[0], "|", r[1], "|", r[2], "|", r[3])

played = wins + losses + draws
percentage = wins / played * 100 if played else 0

print("\nWins:", wins)
print("Losses:", losses)
print("Draws:", draws)
print("Win Percentage:", round(percentage, 1), "%")