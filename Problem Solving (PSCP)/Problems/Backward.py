"""Docstring"""
def main():
    """Moonwalk HeeHee ~"""
    txt_list = []
    while True:
        x = input()
        if x == "NULL":
            break
        txt_list.append(x)
    for i in txt_list[::-1]:
        print(i)
main()
