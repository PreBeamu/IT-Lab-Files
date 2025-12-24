"""Docstring"""
def main():
    """LineSorting!"""
    txt_list = []
    num = int(input())
    for _ in range(num):
        txt = input()
        txt_list.append(txt)
    txt_list.sort(key=len)

    for text in txt_list:
        print(text)

main()
