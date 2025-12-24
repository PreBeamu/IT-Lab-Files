"""Docstring"""
def clamp(value, min_value, max_value):
    """We clamp the value here."""
    return max(min_value, min(value, max_value))

def main():
    """We do funny math to get total prices."""
    meal_price = int(input())
    service = clamp(meal_price*0.1,50,1000)
    vat = (meal_price+service)*0.07
    print(f"{meal_price+service+vat:.2f}")

main()
