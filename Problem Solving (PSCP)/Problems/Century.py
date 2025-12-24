"""Docstring"""
def main():
    """20th Century FOX! Wonder when will it changes to 30th."""
    amount = int(input())
    year_lists = []

    for _ in range(amount):
        year = input().strip()
        year_lists.append(year)

    for i in range(amount):
        year_type = year_lists[i].split()[0]
        year_num = int(year_lists[i].split()[1])

        if not year_type in ("B.E.","A.D."):
            print("ERROR")
            continue
        if year_type == "B.E.":
            year_num -= 543
            if year_num <= 0:
                print("ERROR")
                continue

        century = (year_num-1)//100+1
        print(century)

main()
