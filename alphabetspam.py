s = input()

ws = lc = uc = sym = 0

for c in s:
    if c == "_":
        ws += 1
    elif c in "abcdefghijklmnopqrstuvwxyzåäö":
        lc += 1
    elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ":
        uc += 1
    else:
        sym += 1

print(ws / len(s))
print(lc / len(s))
print(uc / len(s))
print(sym / len(s))