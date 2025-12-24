"""Diabetes."""
import json

def checker(age,sugar):
    """Return result."""
    if 6 <= age <= 13:
        return "eat sugar within the limit" if sugar <= 16 else "eat too much sugar"
    elif 14 <= age < 25:
        return "eat sugar within the limit" if sugar <= 24 else "eat too much sugar"
    elif 25 <= age < 60:
        return "eat sugar within the limit" if sugar <= 16 else "eat too much sugar"
    elif age >= 60:
        return "eat sugar within the limit" if sugar <= 16 else "eat too much sugar"
    else:
        return "error"


def main():
    """Return the answer."""
    data = json.loads(input())
    ex, nex = 0, 0
    for p in data:
        status = checker(int(p["age"]),p["sugar"])
        if status == "eat sugar within the limit":
            nex += 1
        elif status == "eat too much sugar":
            ex += 1
        print(f"{p["name"]} ({int(p["age"])}): {status}")
    print()
    print("Exceed:",ex)
    print("Not Exceed:",nex)


main()
