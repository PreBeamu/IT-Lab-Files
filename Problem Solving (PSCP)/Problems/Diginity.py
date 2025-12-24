"""Docstring"""
def main():
    """Whoops! I forgot your 5 baht.."""
    results = ""
    while True:
        Id = int(input())
        if not Id:
            break
        current_Id = Id
        while True:
            sum_num = 0
            for i in str(current_Id):
                sum_num += int(i)
            current_Id = sum_num
            if sum_num <= 9:
                results += str(sum_num)
                break
    for res in results:
        print(res)

main()
