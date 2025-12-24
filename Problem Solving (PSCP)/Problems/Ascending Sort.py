"""Docstring"""
def main():
    """Sorting stuff here.."""
    num_list = []
    num = int(input())
    for _ in range(num):
        num_list.append(int(input()))
    num_list.sort()
    for i in num_list:
        print(i)
main()
