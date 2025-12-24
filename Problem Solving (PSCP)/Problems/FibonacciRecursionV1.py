"""Docstring"""
def fib(n):
    """Cool Fibonacci!"""
    if not n:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def main():
    """Call Fibonacci!"""
    n = int(input())
    print(fib(n))
main()
