"""Docstring"""
def main():
    """I'm giving this USA cap with Made in china tags a 10/10!"""
    total_rating = float(input())
    highest_rating = float(input())
    remains = total_rating - highest_rating
    mid_rating = min(remains,highest_rating)
    lowest = remains - mid_rating

    if highest_rating - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
