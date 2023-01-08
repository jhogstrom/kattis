d = open(0).read().splitlines()[1:]

for i, _ in enumerate(d, 1):
    days = int(_.split()[1])
    print(i, days + days * (days + 1)//2)
