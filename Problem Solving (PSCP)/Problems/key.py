"""Docstring"""
def main():
    """Da key."""
    key = input()
    yek1 = 0
    for i in key:
        yek1 += int(i)
    yek2 = int(key[-3:]) * 10
    e = str(yek1+yek2)
    print(e[-4:] if int(e)>=1000 else int(e[-4:])+1000)
main()
