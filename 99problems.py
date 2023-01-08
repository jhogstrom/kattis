d = int(input()) + 1

m = (d // 100) * 100
M = m + 100

if m == 0 or M-d <= d-m:
    print(M-1)
else:
    print(m-1)
