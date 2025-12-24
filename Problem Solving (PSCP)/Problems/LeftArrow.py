"""Docstring"""
def main():
    """We make cool arrow that only points to the left."""
    width = int(input())
    height = int(input())
    for i in range(int(height/2),0,-1):
        print(" "*i+"*"*width)
    print("*"*width)
    for i in range(1,int(height/2)+1):
        print(" "*i+"*"*width)

main()
