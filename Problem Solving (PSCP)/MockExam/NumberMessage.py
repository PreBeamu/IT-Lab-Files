"""Number Message."""


def main():
    """Return cool decoded text."""
    msg = input().upper().replace("13", "B").replace("12", "R")
    msg = msg.replace("0", "O").replace("5", "S")
    msg = msg.replace("4", "A").replace("3", "E").replace("1", "I")
    ignore = "123456789"
    for i in ignore:
        msg = msg.replace(i, "")
    print(msg)


main()
