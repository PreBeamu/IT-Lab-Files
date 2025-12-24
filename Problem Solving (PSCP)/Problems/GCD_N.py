"""Docstring"""
def main():
    """Yikes.. there's also V2 version of this code."""
    num_amount = int(input())
    num_list = []
    for _ in range(num_amount):
        num = int(input())
        num_list.append(num)
    num_list.sort()

    gcd = num_list[-1]
    passed = 0
    while gcd > 1:
        for num in num_list:
            if not num%gcd:
                passed += 1
        if passed == num_amount:
            break
        passed = 0
        gcd -= 1

    print(gcd)
main()
