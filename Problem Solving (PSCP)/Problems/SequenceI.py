"""Docstring"""
def main():
    """Matrices give me PTSD.."""
    rows = int(input())
    columns = int(input())
    num = 1
    for _ in range(rows):
        for i in range(columns):
            if i == columns-1:
                print(num)
            else:
                print(num,end = " ")
            num += 1
main()
