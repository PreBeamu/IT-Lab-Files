"""Docstring"""
def main():
    """BIG Matrices give me PTSD.."""
    size = int(input())
    num = 0
    muliplier = 0
    for _ in range(size):
        for i in range(size):
            if i == size-1:
                print(muliplier*size+num)
            else:
                print(muliplier*size+num,end = "-")
                muliplier += 1
        num += 1
        muliplier = 0
        
main()
