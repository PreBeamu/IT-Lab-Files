def calc(n):
    pressed = 0
    length = len(str(n))
    start = 1
    if n == 1:
        print(1)
        return

    for digits in range(1, length):
        end = 10**digits - 1
        count = end - start + 1
        pressed += count * (digits + 1)
        start = 10**digits
    count = n - start + 1
    pressed += count * (length + 1)
    print(pressed)

calc(int(input()))
