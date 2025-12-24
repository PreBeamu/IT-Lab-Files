"""Docstring"""
def main():
    """Short! Long! Short! Hort! Wait what?.."""
    shorten = ""
    last_num = -1
    actual_last = ""

    while True:
        x = int(input())
        if x < 0:
            if shorten.endswith('-'):
                shorten += actual_last
            break

        if x > last_num + 1:
            if shorten.endswith('-'):
                shorten += actual_last
            if shorten:
                shorten += f", {x}"
            else:
                shorten = f"{x}"
        else:
            if not shorten.endswith('-'):
                shorten += '-'
            actual_last = str(x)
        last_num = x
    print(shorten)

main()
