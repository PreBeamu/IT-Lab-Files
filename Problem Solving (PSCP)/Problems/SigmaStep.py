"""Docstring"""
def main():
    """Sigma stepping very Sigma."""
    start = int(input())
    end = int(input())
    step = int(input())

    if not step:
        if start == end:
            print(start)
        else:
            print("error")
        return
    if (start < end and step < 0) or (start > end and step > 0):
        print("error")
        return

    total = 0
    current = start
    if step > 0:
        while current <= end:
            total += current
            current += step
    else:
        while current >= end:
            total += current
            current += step
    print(total)

main()
