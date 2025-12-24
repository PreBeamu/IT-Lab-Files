"""Docstring"""
memo = {}

def fib(n):
    """Cool Fibonacci!"""
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

def repeat_add(x, times):
    """* Got Banned!"""
    if times <= 0:
        return 0
    return x + repeat_add(x, times - 1)

def main():
    """Call Fibonacci!"""
    n = int(input())
    fib(repeat_add(int(n / 20), 1) + 1)
    fib(repeat_add(int(n / 20), 2) + 1)
    fib(repeat_add(int(n / 20), 3) + 1)
    fib(repeat_add(int(n / 20), 4) + 1)
    fib(repeat_add(int(n / 20), 5) + 1)
    fib(repeat_add(int(n / 20), 6) + 1)
    fib(repeat_add(int(n / 20), 7) + 1)
    fib(repeat_add(int(n / 20), 8) + 1)
    fib(repeat_add(int(n / 20), 9) + 1)
    fib(repeat_add(int(n / 20), 10) + 1)
    fib(repeat_add(int(n / 20), 11) + 1)
    fib(repeat_add(int(n / 20), 12) + 1)
    fib(repeat_add(int(n / 20), 13) + 1)
    fib(repeat_add(int(n / 20), 14) + 1)
    fib(repeat_add(int(n / 20), 15) + 1)
    fib(repeat_add(int(n / 20), 16) + 1)
    fib(repeat_add(int(n / 20), 17) + 1)
    fib(repeat_add(int(n / 20), 18) + 1)
    fib(repeat_add(int(n / 20), 19) + 1)
    fib(repeat_add(int(n / 20), 20) + 1)
    print(fib(n))
main()
