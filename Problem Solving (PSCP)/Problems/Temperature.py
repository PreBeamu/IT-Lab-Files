"""Docstring"""
def main():
    """We use math to make thing works here."""
    temp = float(input())
    from_type = input()
    convert_to = input()
    celcius = 0
    if from_type.upper() == "C":
        celcius = temp
    elif from_type.upper() == "K":
        celcius = temp-273.15
    elif from_type.upper() == "F":
        celcius = (temp-32)*5/9
    elif from_type.upper() == "R":
        celcius = (5*temp)/9-273.15

    if convert_to.upper() == "C":
        print(f"{celcius:.2f}")
    elif convert_to.upper() == "K":
        print(f"{celcius+273.15:.2f}")
    elif convert_to.upper() == "F":
        print(f"{celcius*9/5+32:.2f}")
    elif convert_to.upper() == "R":
        print(f"{(celcius+273.15)*9/5:.2f}")

main()
