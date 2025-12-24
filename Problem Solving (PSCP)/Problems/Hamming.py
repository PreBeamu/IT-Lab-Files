"""Docstring"""
def main():
    """Ham bacon Fried egg.. wait what?"""
    txt1 = input()
    txt2 = input()
    length = len(txt1)
    same = 0
    for i in range(length):
        if txt1[i] != txt2[i]:
            same += 1
    print(same)

main()
