"""Docstring"""
def main():
    """We make cool triangle."""
    height = int(input())
    for i in range(1, height + 1):
        if i == 1:
            print("0")
        elif i == 2:
            print("0 0")
        elif i == height:
            print("0 " * (i - 1) + "0")
        else:
            middle = "1 " * (i - 2)
            print("0 " + middle + "0")

main()
