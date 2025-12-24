"""Docstring"""
def main():
    """mm.. Donuts, We all love donuts!"""
    price = int(input()) # Prices per Donut
    pro_required = int(input()) # Donut free
    free = int(input()) # Amount of free Donut
    minimum = int(input()) # Donuts Needed
    bought_donut = 0
    free_donut = 0

    while minimum > 0:
        bought_donut += 1
        if not bought_donut % pro_required:
            free_donut += free
        if bought_donut+free_donut >= minimum:
            break

    print(bought_donut*price,bought_donut+free_donut)

main()
