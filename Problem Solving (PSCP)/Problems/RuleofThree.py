"""Docstring"""
def main():
    """We're saving 99.99% of our money with this one!"""
    variants = int(input())
    best_one = ""
    last_num = float('inf')
    last_price = float('inf')

    for _ in range(variants):
        price = float(input())
        weight = float(input())
        if (price/weight) < last_num:
            last_price = price
            last_num = price/weight
            best_one = str(f"{price:.2f} {weight:.2f}")
        elif (price/weight) == last_num:
            if price < last_price:
                last_price = price
                last_num = price/weight
                best_one = str(f"{price:.2f} {weight:.2f}")

    print(best_one)

main()
