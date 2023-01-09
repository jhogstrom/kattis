# https://open.kattis.com/problems/asciiaddition

data = open(0).read().splitlines()
numbers = {
    '0': [
        "xxxxx",
        "x...x",
        "x...x",
        "x...x",
        "x...x",
        "x...x",
        "xxxxx",
    ],
    '1': [
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
    ],
    '2': [
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
        "x....",
        "x....",
        "xxxxx",
    ],
    '3': [
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
    ],
    '4': [
        "x...x",
        "x...x",
        "x...x",
        "xxxxx",
        "....x",
        "....x",
        "....x",
    ],
    '5': [
        "xxxxx",
        "x....",
        "x....",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
    ],
    '6': [
        "xxxxx",
        "x....",
        "x....",
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
    ],
    '7': [
        "xxxxx",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
    ],
    '8': [
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
    ],
    '9': [
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
    ],
    "plus": [
        ".....",
        "..x..",
        "..x..",
        "xxxxx",
        "..x..",
        "..x..",
        ".....",
    ],
}


def extract_symbol(data, i):
    sym = []
    for j in range(7):
        sym.append(data[j][i:i+5])
    for s, charmap in numbers.items():
        if sym == charmap:
            return s
    raise ValueError(f"Unable to find {sym}")


symbols, i = [], 0


while i < len(data[0]):
    symbols.append(extract_symbol(data, i))
    i += 6

t1, t2, uset2 = "", "", False

for s in symbols:
    if s == "plus":
        uset2 = True
        continue
    if uset2:
        t2 += s
    else:
        t1 += s

res = str(int(t1) + int(t2))
for r in range(7):
    out = []
    for c in res:
        out.append(numbers[c][r])
    print(".".join(out))
