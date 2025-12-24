"""Best_Before."""

def main():
    """Return the answer."""
    amount = int(input())
    seen_mm, seen_dd = False, False
    for _ in range(amount):
        x = input()
        if int(x[:2]) > 12:
            seen_dd = True
        if int(x[2:4]) > 12:
            seen_mm = True
    if seen_dd and not seen_mm:
        print("ddmmyy")
    elif seen_mm and not seen_dd:
        print("mmddyy")
    else:
        print("no clue")

main()
