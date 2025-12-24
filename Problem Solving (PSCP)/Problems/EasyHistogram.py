"""Docstring"""
def main():
    """Easy Histogram!"""
    msg = input()
    letters = {}
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    for i in msg:
        if not i.isalpha():
            continue
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    for x in alphabet:
        if x in letters:
            print(x,"=",letters[x])

main()
