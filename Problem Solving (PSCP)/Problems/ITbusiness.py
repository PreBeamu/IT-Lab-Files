"""Docstring"""
def main():
    """We're getting rich with this one bois."""
    money = float(input())
    cash = float(input())
    action = ""
    malfunction_count = 0

    while action != "end" and malfunction_count < 3:
        action = input()
        if action == "end" or not action:
            break
        curr_action = action[0]
        amount = float(action[2:])
        if curr_action == "W":
            if money >= amount:
                money -= amount
                cash += amount
                malfunction_count = 0
            else:
                malfunction_count += 1
        elif curr_action == "D":
            if cash >= amount:
                cash -= amount
                money += amount
                malfunction_count = 0
            else:
                malfunction_count += 1

    print(f"{money:.2f}")
    print(f"{cash:.2f}")

main()
