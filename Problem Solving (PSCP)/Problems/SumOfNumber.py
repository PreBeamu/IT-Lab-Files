"""Docstring"""
def main():
    """Docstring"""
    num = []
    sum_want = int(input())
    while True:
        x = int(input())
        if x == -1:
            break
        num.append(x)
        if sum(num) == sum_want:
            break
    print(sum(num))

main()
