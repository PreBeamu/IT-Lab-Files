"""Docstring"""
def main():
    """What did 113 do to deserve this? TwT"""
    num = str(input())
    while "113" in num:
        num = num.replace("113","")
    print(num.replace("113",""))

main()
