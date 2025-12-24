"""Docstring"""
def main():
    """We find big number."""
    num1 = input()
    num2 = input()
    num3 = input()
    c1 = num1 + num2 + num3
    c2 = num1 + num3 + num2
    c3 = num2 + num1 + num3
    c4 = num2 + num3 + num1
    c5 = num3 + num1 + num2
    c6 = num3 + num2 + num1
    biggest = c1

    if c2 > biggest:
        biggest = c2
    if c3 > biggest:
        biggest = c3
    if c4 > biggest:
        biggest = c4
    if c5 > biggest:
        biggest = c5
    if c6 > biggest:
        biggest = c6

    print(int(biggest))

main()
