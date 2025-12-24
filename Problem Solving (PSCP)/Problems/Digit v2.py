"""Docstring"""
def main():
    """How much is this?"""
    read = input().split()
    numbers = ["zero","one","two","three","four","five",
               "six","seven","eight","nine"]
    two_d = ["ten","eleven","twelve","thirteen","fourteen",
    "fifteen","sixteen","seventeen","eighteen","nineteen",
    "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if "thousand" in read:
        print(4)
        return
    if "hundred" in read:
        print(3)
        return
    for i in two_d:
        if i in read:
            print(2)
            return
    for i in numbers:
        if i in read:
            print(1)
            return
main()
