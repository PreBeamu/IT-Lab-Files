"""Docstring"""
def main():
    """Cool math that I don't even know how it works."""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5
    radius_sum = r1+r2
    if distance > radius_sum:
        print("no overlapping")
    else:
        print("overlapping")

main()
