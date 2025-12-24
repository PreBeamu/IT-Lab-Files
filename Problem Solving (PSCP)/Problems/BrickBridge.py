"""Docstring"""
def main():
    """Brick by brick we build a brigde!"""
    small = int(input()) # 1 inch
    large = int(input()) # 5 inch
    goal = int(input())

    used_large = min(goal//5, large)
    used_small = goal-used_large*5

    if used_small <= small:
        print(used_small)
    else:
        print(-1)

main()
