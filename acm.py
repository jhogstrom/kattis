from collections import defaultdict


data = open(0).read().splitlines()[:-1]

solved = {}
attempts = defaultdict(int)
for _ in data:
    t, p, res,  = _.split()
    if res == "right":
        solved[p] = int(t)
    else:
        attempts[p] += 1

score = 0
for p, t in solved.items():
    score += t + attempts[p] * 20


print(len(solved), score)
