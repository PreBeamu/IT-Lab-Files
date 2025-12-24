"""Remove Digits."""

def main():
    """Return the answer."""
    num = input()
    options, queue = [], []
    index = 0
    while len(str(num)) > 1:
        for i in num:
            if index > 0:
                options.append(num[index-1]+i)
            index += 1
        index = 0
        for i in options:
            queue.append(num.replace(i,""))
        options = []
        num = max(queue)
        queue = []
    print(num)

main()
