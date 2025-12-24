"""Docstring"""
def main():
    """3nPlus1!"""
    num_list = []
    while True:
        num = int(input())
        if not num:
            break
        num_list.append(num)

    for curr_num in num_list:
        n = curr_num
        times = 1
        while n > 1:
            if not n%2:
                n /= 2
            else:
                n = n*3+1
            times += 1
        print(times)

main()
