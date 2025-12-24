"""Docstring"""
def main():
    """It's christmas! Wait..
    I don't think that pine tree is supposed to be in the temple."""
    start_color = input().upper()
    amount = int(input())
    colors = {
        "R": ["Red", "Green", "Blue"],
        "G": ["Green", "Blue", "Red"],
        "B": ["Blue", "Red", "Green"]
        }[start_color]

    result = []
    for i in range(amount):
        result.append(colors[i%3])
    print(" ".join(result))

main()
