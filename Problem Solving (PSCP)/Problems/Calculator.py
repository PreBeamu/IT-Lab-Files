"""Docstring"""
def main():
    """main Function forever!"""
    n = int(input())
    current_num = 0
    pressed = 0
    for _ in range(n):
        current_num += 1
        pressed += len(str(current_num))+1
    if n == 1:
        pressed = 1
    print(pressed)

main()
