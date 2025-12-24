"""Docstring"""
def main():
    """Card game again?.."""
    amount = int(input())
    cards = []
    score = 0
    aces = 0
    for _ in range(amount):
        card = input()
        cards.append(card)
    for i in cards:
        if i == "A":
            aces += 1
        elif i in "JQK":
            score += 10
        else:
            score += int(i)
    for _ in range(aces):
        if score + 11 <= 21 - (aces-1):
            score += 11
        else:
            score += 1
        aces -= 1
    print(score)
main()
