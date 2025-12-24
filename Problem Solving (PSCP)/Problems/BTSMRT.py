"""Docstring"""
def main():
    """BTS MRT goes vroom vroom!"""
    special_day = input().title()
    passenger_age = float(input())
    height = float(input())
    payment = "PAY"

    if passenger_age < 14 and height <= 140 and special_day == "Children Day":
        payment = "FREE"
    if passenger_age < 14 and height < 90:
        payment = "FREE"

    if passenger_age >= 60 and special_day == "Senior Day":
        payment = "FREE"

    print(payment)



main()
