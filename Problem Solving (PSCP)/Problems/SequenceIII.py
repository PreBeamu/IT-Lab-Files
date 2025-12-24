"""Docstring"""
def main():
    """SEQUENCES give me PTSD!!"""
    num = int(input())
    base_num = 1
    for _ in range(num):
        for i in range(1,num+1):
            if i == num:
                print(base_num+i)
            else:
                print(base_num+i,end=" ")
        base_num += 1

main()
