"""Docstring"""
def main():
    """SEQUENCES give me PTSD!!"""
    num = int(input())
    for i in range(1,num+1):
        if not i%7:
            print((num+1)-i)
        else:
            print((num+1)-i,end=" ")

main()
