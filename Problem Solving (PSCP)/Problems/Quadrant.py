"""Docstring"""
def main():
    """That's alot of if statements!"""
    x = int(input())
    y = int(input())
    x_Pos = x > 0
    y_Pos = y > 0

    if not x and not y:
        print("O")
    elif not x and y:
        print("Y")
    elif not y and x:
        print("X")
    elif x_Pos and y_Pos:
        print("Q1")
    elif not x_Pos and y_Pos:
        print("Q2")
    elif not x_Pos and not y_Pos:
        print("Q3")
    elif x_Pos and not y_Pos:
        print("Q4")

main()
