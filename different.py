data = open(0).read().splitlines()

for _ in data:
    a, b = [int(t) for t in _.split()]
    print(abs(a-b))