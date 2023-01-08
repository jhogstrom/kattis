# https://open.kattis.com/submissions/10199948
data = open(0).read().splitlines()
n, _ = [int(_) for _ in data[0].split()]

teams = [f"T{_+1}" for _ in range(n)]
for game in data[1:]:
    winner, loser = game.split()
    wi, li = teams.index(winner), teams.index(loser)
    if li > wi:
        continue
    teams.pop(li)
    teams.insert(wi, loser)

print(" ".join(teams))
