n, s, m = [int(_) for _ in input().split()]
board = [int(_) for _ in input().split()]
p, visited = s-1, []


def done(msg):
    print(msg)
    print(len(visited))
    exit()


while True:
    # print(f"Landing on {board[p]} @ {p}")
    if p < 0:
        done("left")
    elif p >= len(board):
        done("right")
    elif board[p] == m:
        done("magic")
    elif p in visited:
        done("cycle")
    visited.append(p)
    p += board[p]
