"""Docstring"""

def main():
    """Coding a program to cheat the magician is crazy work."""
    swap_code = input().upper()
    current_ball = 1
    for i in swap_code:
        if i == "A":
            if current_ball == 1:
                current_ball = 2
            elif current_ball == 2:
                current_ball = 1
        elif i == "B":
            if current_ball == 2:
                current_ball = 3
            elif current_ball == 3:
                current_ball = 2
        elif i == "C":
            if current_ball == 3:
                current_ball = 1
            elif current_ball == 1:
                current_ball = 3
    print(current_ball)

main()
