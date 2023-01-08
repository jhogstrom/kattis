monthly, count, *data = [int(_) for _ in open(0).read().splitlines()]

total = monthly * (count+1)
print(total - sum(data))
