"""Docstring"""
def main():
    """GQuuuuuuX!!"""
    shout = input().lower()
    highest_u = 0
    i = 0
    n = len(shout)

    while i < n:
        if i + 1 < n and shout[i] == 'g' and shout[i + 1] == 'q':
            i += 2
            count_u = 0
            while i < n and shout[i] == 'u':
                count_u += 1
                i += 1
            if i < n and shout[i] == 'x':
                highest_u = max(highest_u, count_u)
        else:
            i += 1
    print(highest_u if highest_u > 0 else "None")
main()
