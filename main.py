game_rounds = []
score = 0
strategy_key = {"A Y": 8,
                "B Z": 9,
                "C X": 7,
                "A Z": 3,
                "B X": 1,
                "C Y": 2,
                "A X": 4,
                "B Y": 5,
                "C Z": 6}

with open("abc_xyz.txt", "r") as file:
    for line in file:
        game_rounds.append(line)

for item in game_rounds:
    score = score + strategy_key.get(item.partition("\n")[0])
print(score)

