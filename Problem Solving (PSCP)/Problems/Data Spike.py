"""Docstring"""
def main():
    """DataSpike!"""
    num_list = []
    for _ in range(8):
        num = int(input())
        num_list.append(num)

    highest = num_list[0]
    for i in num_list:
        if i > highest:
            highest = i
    print(highest)

main()
