"""Docstring"""
def main():
    """SEQUENCES give me PTSD!!"""
    num = int(input())
    digits = 1
    for _ in range(num-1):
        for x in range(1,digits+1):
            if x == digits:
                print(x)
            else:
                print(x,end=" ")
        digits += 1
    digits = num
    for _ in range(num):
        for x in range(1,digits+1):
            if x == digits:
                print(x)
            else:
                print(x,end=" ")
        digits -= 1

main()
