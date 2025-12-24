"""Docstring"""
def main():
    """Pick them!! but again!.."""
    my_list = list(input().split())
    true_nums = []
    for i in my_list:
        if not int(i)%3 or not int(i)%5:
            true_nums.append(i)
    if len(true_nums) <= 0:
        print("Nope")
        return
    for num in true_nums[::-1]:
        print(num)

main()
