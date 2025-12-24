"""Docstring"""
def main():
    """We make cool arrow that only points to the right."""
    width = int(input())
    height = int(input())
    for i in range(0,int(height/2)):
        print(" "*i+"*"*width)
    print(" "*int(height/2)+"*"*width)
    for i in range(int(height/2),0,-1):
        print(" "*(i-1)+"*"*width)

main()
