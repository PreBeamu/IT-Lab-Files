"""Docstring"""
def main():
    """Encoding!!"""
    passkey = input()
    lastLetter = passkey[0]
    amount = 0
    result = ""
    for letter in passkey:
        if letter == lastLetter:
            amount += 1
        else:
            result += str(amount)+lastLetter
            lastLetter = letter
            amount = 1
    result += str(amount)+lastLetter
    print(result)

main()
