"""Docstring"""
def main():
    """Median!"""
    data = input().split(", ")
    data = [ float(i) for i in data ]
    data.sort()
    mid_index = len(data)//2
    if not len(data)%2:
        print(f"{((data[mid_index-1])+(data[mid_index]))/2:.2f}")
    else:
        print(f"{data[mid_index]:.2f}")
main()
