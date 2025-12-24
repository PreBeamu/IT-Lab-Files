"""Coffee Shop."""


def main():
    """Return the best deal."""
    price_per_cup = float(input())
    discount = float(input())
    special_discount = float(input())
    special_price_req = float(input())
    want = int(input())
    pro_1 = 0
    pro_2 = 0
    total = 0
    for current in range(want):
        total += price_per_cup
        if not current:
            pro_1 += price_per_cup
        else:
            pro_1 += price_per_cup-(price_per_cup*(discount/100))
    if total >= special_price_req:
        pro_2 = total-(total*(special_discount/100))
    else:
        pro_2 = total
    if pro_1 < pro_2:
        print(1)
        print(f"{pro_1:.2f}")
    elif pro_2 < pro_1:
        print(2)
        print(f"{pro_2:.2f}")
    else:
        print(2)
        print(f"{pro_2:.2f}")


main()
