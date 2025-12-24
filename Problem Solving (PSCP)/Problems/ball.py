"""Docstring"""
def main():
    """Guess who's going to make world's first inf bouncing ball."""
    release_point = float(input())
    last_bounce = release_point
    count = -1
    while True:
        if last_bounce < 0.01:
            break
        last_bounce *= 3/5
        count+=1
    print(count)

main()
