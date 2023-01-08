data = open(0).read().splitlines()[1:]
for _ in data:
    v = [int(v) for v in _.split(" ")]
    avg = sum(v[1:]) / v[0]
    above = len([r for r in v[1:] if r > avg])
    print(f"{100*above/v[0]:.3f}%")