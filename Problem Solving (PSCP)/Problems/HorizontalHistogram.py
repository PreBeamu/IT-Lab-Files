"""Docstring"""
def main():
    """Horizontal Histogram!"""
    msg = input()
    letters = {}
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Count Letters and sort.
    for i in msg:
        letters[i] = msg.count(i)
    for x in alphabet:
        if x in letters:
            dashes = ""
            for i in range(letters[x]):
                dashes += "-"
                if not len(dashes.replace("|",""))%5:
                    dashes += "|"
            print(x,": "+(dashes.rstrip("|")))

main()
