_, step = [int(_) for _ in input().split()]
print(" ".join([_ for _ in input().split()[step-1::step]]))
