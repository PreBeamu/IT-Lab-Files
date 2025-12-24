"""Docstring"""
def main():
    """What's the missing one?"""
    amount = int(input())
    num_list = []
    while 0 not in num_list:
        num = int(input())
        num_list.append(num)
    num_list.sort()
    for i in range(num_list[0],amount+1):
        if i not in num_list:
            print(i)
main()
