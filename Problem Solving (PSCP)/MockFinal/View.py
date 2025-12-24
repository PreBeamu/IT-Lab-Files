"""View Cubes"""

def main():
    """Return the answer."""
    n = int(input())
    m = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    side = input().strip()
    max_height = max(max(row) for row in data)

    box = [[" " for _ in range(m if side in ("Front", "Back") else n)]
           for _ in range(max_height)]

    if side == "Front":
        for col in range(m):
            mh = max(data[row][col] for row in range(n))
            for h in range(mh):
                box[max_height - 1 - h][col] = "x"

    elif side == "Back":
        for col in range(m):
            mh = max(data[row][col] for row in range(n))
            for h in range(mh):
                box[max_height - 1 - h][m - 1 - col] = "x"

    elif side == "Left":
        for row in range(n):
            mh = max(data[row])
            for h in range(mh):
                box[max_height - 1 - h][row] = "x"

    elif side == "Right":
        for row in range(n):
            mh = max(data[row])
            for h in range(mh):
                box[max_height - 1 - h][n - 1 - row] = "x"

    for line in box:
        print(" ".join(line).rstrip())

main()
