"""Docstring"""
def main():
    """I've also never played any cards."""
    key = input().upper()
    names = {
        "A":"Ace",
        "J":"Jack",
        "Q":"Queen",
        "K":"King",
        "D":"Diamonds",
        "H":"Hearts",
        "S":"Spades",
        "C":"Clubs",
    }
    result = ""
    for i in key:
        if i.isnumeric():
            result += i
            continue
        if names[i]:
            if "of" not in result and result:
                result += " of "
            result += names[i]
            if "of" not in result:
                result += " of "
    print(result)

main()
