"""Docstring"""
def main():
    """Wah! I don't like how this game works."""
    x = int(input())
    if not x%3 or str(x)[-1] == "3":
        print("PONG")
    else:
        print(x)

main()
