"""Docstring"""
def main():
    """Lets gooo we're finding leapYear with this one."""
    BC = int(input())
    if BC % 100:
        if not BC % 4:
            print(f"{str(BC)} is a leap year.")
        else:
            print(f"{str(BC)} is not a leap year.")
    else:
        if not BC % 400:
            print(f"{str(BC)} is a leap year.")
        else:
            print(f"{str(BC)} is not a leap year.")

main()
