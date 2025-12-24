"""Docstring"""
def main():
    """Coke IT Edition promotion very cool!"""
    price = int(input())
    caps_required = int(input())
    discount_price = int(input())
    amount = int(input())

    discounted_bottles = 0
    current_caps = 0
    if caps_required > 0:
        for _ in range(amount):
            if current_caps >= caps_required:
                discounted_bottles += 1
                current_caps = 0
            current_caps += 1
    original_prices = price*(amount-discounted_bottles)

    print(original_prices+(discounted_bottles*discount_price))

main()
