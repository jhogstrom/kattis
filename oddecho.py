_, *w = open(0).read().splitlines()
print("\n".join(_ for _ in w[::2]))