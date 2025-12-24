"""Docstring"""

def is_even(num):
    """Check even!"""
    return num & 1 == 0

print(is_even(int(input())))

def ex_2(n):
    if n == 0:
        print("Go Back!")
    else:
        print(str(n)+" - Go Up!")
        ex_2(n-2)
        print(str(n)+" - Go Down!")

ex_2(6)
