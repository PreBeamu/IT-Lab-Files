"""Docstring"""
def main():
    """hacker man ~ Hacker man!"""
    shift = int(input())
    text = input()
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    print(result)

main()
