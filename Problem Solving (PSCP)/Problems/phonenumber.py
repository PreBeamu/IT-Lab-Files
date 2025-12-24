"""Docstring"""
def main():
    """Brr Brr.. Your phone linging!"""
    number = input()
    num_type = input()
    if len(number) == 9:
        if num_type == "Domestic":
            print(number[0],number[1:5],number[5:])
        elif num_type == "International":
            print("+66",number[1:5],number[5:])
    elif len(number) == 10:
        if num_type == "Domestic":
            print(number[:2], number[2:6], number[6:])
        elif num_type == "International":
            print("+66" + number[1], number[2:6], number[6:])

main()
