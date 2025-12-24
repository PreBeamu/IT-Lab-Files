"""Docstring"""

def main():
    """I don't like inflation.."""
    price = int(float(input()) * 100)
    years_passed = int(input())
    price_after = price
    for _ in range(years_passed):
        inflate = (price_after * 381) // 10000
        price_after += inflate
    baht = price_after // 100
    satang = price_after % 100
    print(f"{baht}.{satang:02d}")
main()
