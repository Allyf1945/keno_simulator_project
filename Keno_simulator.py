import random

player_numbers = [2, 5, 7, 13, 35, 47, 49, 77, 79, 80]

total_games = 10000

eight_matches = 0
nine_matches = 0
ten_matches = 0

for game in range(total_games):

    winning_numbers = random.sample(range(1, 81), 20)

    matches = 0

    for number in player_numbers:
        if number in winning_numbers:
            matches += 1

    if matches == 8:
        eight_matches += 1

    elif matches == 9:
        nine_matches += 1

    elif matches == 10:
        ten_matches += 1

print("Keno Simulation Results")
print(f"Total Games Simulated: {total_games}")
print(f"8 Matches: {eight_matches}")
print(f"9 Matches: {nine_matches}")
print(f"10 Matches (Jackpots): {ten_matches}")
