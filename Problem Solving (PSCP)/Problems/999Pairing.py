"""Docstring"""
def main():
    """It's over 900!"""
    digits = int(input())
    code1 = input()
    code2 = input()

    failed = 0
    for i in range(digits):
        if int(code1[i]) + int(code2[i]) != 9:
            failed += 1

    print("YES" if not failed else f"NO {failed}")

main()
