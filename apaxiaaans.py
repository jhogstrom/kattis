# https://open.kattis.com/problems/apaxiaaans
s = input()

res = [s[0]]
for c in s[1:]:
    if c != res[-1]:
        res.append(c)

print("".join(res))
