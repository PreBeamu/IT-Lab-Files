"""Docstring"""
def main():
    """We be doing five five X X."""
    num = int (input())
    for i in range(1,num+1):
        print("*" if i%5 else "X",end="")

main()
