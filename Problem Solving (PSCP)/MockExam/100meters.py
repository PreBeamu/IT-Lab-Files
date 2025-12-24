"""100 meters."""


def main():
    """Look for best runner."""
    r1 = f"{float(input())}"
    r2 = f"{float(input())}"
    r3 = f"{float(input())}"
    r4 = f"{float(input())}"
    r5 = f"{float(input())}"
    r6 = f"{float(input())}"
    r7 = f"{float(input())}"
    r8 = f"{float(input())}"
    data = r1+"#"+r2+"#"+r3+"#"+r4+"#"+r5+"#"+r6+"#"+r7+"#"+r8+"#"
    first, second, third = float('inf'), float('inf'), float('inf')
    first_r, second_r, third_r = 0, 0, 0
    # Find First
    current = ""
    runner = 0
    for i in data:
        if i == "#":
            runner += 1
            if float(current) < first:
                first = float(current)
                first_r = runner
            current = ""
            continue
        current += i
    # Find Second
    current = ""
    runner = 0
    for i in data:
        if i == "#":
            runner += 1
            if float(current) < second and float(current) > first:
                second = float(current)
                second_r = runner
            current = ""
            continue
        current += i
    # Find Third
    current = ""
    runner = 0
    for i in data:
        if i == "#":
            runner += 1
            if float(current) < third and float(current) > second:
                third = float(current)
                third_r = runner
            current = ""
            continue
        current += i
    print(first_r, second_r, third_r)


main()
