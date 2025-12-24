"""Docstring"""

def gcd(a,b):
    """GCD func!"""
    if not b:
        return a
    return gcd(b, a % b)

print(gcd(int(input()), int(input())))