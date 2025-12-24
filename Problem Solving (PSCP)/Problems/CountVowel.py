"""Docstring"""
def main():
    """We count stuff here!"""
    letters = int(input())
    vowels = 0
    for _ in range(letters):
        alphabet = input().upper()
        if alphabet in ['A','E','I','O','U']:
            vowels += 1
    print(vowels)

main()
