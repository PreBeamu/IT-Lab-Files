"""Docstring"""
def main():
    """SEQUENCES give me PTSD!!"""
    num = int(input())
    digits = 1
    for _ in range(num):
        for x in range(1,digits+1):
            if x == digits:
                print(x)
            else:
                print(x,end=" ")
        digits += 1

main()
