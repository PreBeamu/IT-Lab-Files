"""Post Office."""


def main():
    """Return the price required for package."""
    n = int(input())
    m = int(input())
    total_env = n*13
    total_box = m*15
    for _ in range(n):
        w = float(input())
        if w > 1000:
            total_env += 68
        elif w > 500:
            total_env += 48
        elif w > 250:
            total_env += 33
        elif w > 100:
            total_env += 28
        elif w > 20:
            total_env += 23
        elif w > 10:
            total_env += 18
        else:
            total_env += 16
    for _ in range(m):
        w = float(input())
        if w > 1000:
            total_box += 70
        elif w > 500:
            total_box += 55
        else:
            total_box += 45
    print(total_env+total_box)


main()
