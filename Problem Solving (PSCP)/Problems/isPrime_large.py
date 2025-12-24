"""Docstring"""
def main():
    """We look for prime numbers."""
    num = int(input())
    if num < 2:
        print("NO")
        return
    for i in range(2, int((num)**0.5) + 1):
        if not num % i:
            print("NO")
            return
    print("YES")

main()
