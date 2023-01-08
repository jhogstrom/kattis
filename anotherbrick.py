# https://open.kattis.com/problems/anotherbrick
h, w, n = [int(_) for _ in input().split()]
bricks = [int(_) for _ in input().split()]

height, width = 0, 0
while bricks:
    width += bricks.pop(0)
    if width < w:
        continue
    if width == w:
        height += 1
        width = 0
        if height == h:
            print("YES")
            exit()
        continue
    print("NO")
    break
