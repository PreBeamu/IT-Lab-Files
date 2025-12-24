"""Docstring"""
def main():
    """It's SUMMER TIME!"""
    month = int(input())
    day = int(input())
    seasons = ["winter","spring","summer","fall"]
    if not month % 3 and day >= 21:
        seasons = ["spring","summer","fall","winter"]

    if month <= 3:
        print(seasons[0])
    elif month <= 6:
        print(seasons[1])
    elif month <= 9:
        print(seasons[2])
    elif month <= 12:
        print(seasons[3])

main()
