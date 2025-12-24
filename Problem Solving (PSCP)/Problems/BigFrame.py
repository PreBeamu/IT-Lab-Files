"""Docstring"""
def add_whitespaces(longest,txt):
    """Check if text need more whitespaces!"""
    if len(txt) >= longest:
        print("* "+txt+" *")
    else:
        txt += " "*(longest-len(txt))
        print("* "+txt+" *")

def main():
    """We do big frame to handle the texts!"""
    text1 = input().strip()
    text2 = input().strip()
    text3 = input().strip()
    text4 = input().strip()
    text5 = input().strip()
    longest = 0

    if len(text1) > longest:
        longest = len(text1)
    if len(text2) > longest:
        longest = len(text2)
    if len(text3) > longest:
        longest = len(text3)
    if len(text4) > longest:
        longest = len(text4)
    if len(text5) > longest:
        longest = len(text5)

    print("*"*(longest+4))

    if len(text1) > longest:
        longest = len(text1)
    if len(text2) > longest:
        longest = len(text2)
    if len(text3) > longest:
        longest = len(text3)
    if len(text4) > longest:
        longest = len(text4)
    if len(text5) > longest:
        longest = len(text5)

    add_whitespaces(longest,text1)
    add_whitespaces(longest,text2)
    add_whitespaces(longest,text3)
    add_whitespaces(longest,text4)
    add_whitespaces(longest,text5)

    print("*"*(longest+4))

main()
