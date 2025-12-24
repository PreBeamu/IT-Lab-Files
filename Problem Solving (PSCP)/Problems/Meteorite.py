"""Docstring"""
def main():
    """It's going to hit the earth! But who cares.."""
    weight = float(input())
    split = int(input())
    safe_weight = float(input())
    weapons_fired = 0
    current_debris = 1

    while current_debris:
        if weight >= safe_weight:
            weapons_fired += current_debris
            weight /= split
            current_debris *= split
            # print("CURRENT DEBRIS:",current_debris)
            # print("CURRENT WEIGHT:",weight)
        else:
            break

    # print("FIRED!:",weapons_fired)
    print(weapons_fired)
main()
