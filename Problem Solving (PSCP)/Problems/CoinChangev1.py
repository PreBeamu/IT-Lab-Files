"""Docstring"""
def main():
    """Whoops! I forgot your 5 baht.."""
    paid = int(input())
    coins = [25,10,5,1]
    change = 0
    for i in coins:
        if paid < 1:
            break
        change += paid//i
        paid -= (paid//i)*i
    print(change)

main()
