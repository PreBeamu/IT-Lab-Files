"""Game."""


def main():
    """Return possible tie games."""
    total_a = int(input())
    total_b = int(input())
    highest = max(total_a, total_b)
    lowest = min(total_a, total_b)
    ties_a = highest % 3
    ties_b = lowest % 3
    if ties_a != ties_b:
        print("Error")
        return
    print(ties_a)


main()
