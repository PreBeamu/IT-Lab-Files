"""Docstring"""
def main():
    """Yikes.. there's also V1 version of this code.
    also Euclidean Algorithm is very pog!"""
    numbers = []
    for _ in range(2):
        num = int(input())
        numbers.append(num)
    numbers.sort()

    last_ans = numbers[1]
    remainder = 1
    while True:
        if 0 in numbers:
            break
        remainder = numbers[0]%numbers[1]
        numbers[0] = numbers[1]
        numbers[1] = remainder
        if not remainder:
            break
        last_ans = remainder
    print(last_ans)
main()
