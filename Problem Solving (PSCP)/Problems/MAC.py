"""Docstring"""
def check_errors(dash_found, colon_found, dot_found, last_block, parts_count):
    """Check for Possible Errors!"""
    if (dash_found > 0) + (colon_found > 0) + (dot_found > 0) > 1:
        print("ERROR")
        return True
    if dot_found > 2 or dash_found > 5 or colon_found > 5:
        print("ERROR")
        return True
    if not last_block or (last_block not in [2,4]):
        print("ERROR")
        return True
    if dash_found > 0 or colon_found > 0:
        if parts_count != 6:
            print("ERROR")
            return True
    elif dot_found > 0:
        if parts_count != 3:
            print("ERROR")
            return True
    else:
        print("ERROR")
        return True
    return False

def main():
    """MAC Cheeseburger!"""
    mac = input().strip() + " "
    dash_found = colon_found = dot_found = 0
    last_block = block = 0
    parts_count = 0

    for i in mac:
        if i in "-:. ":
            dash_found += i == "-"
            colon_found += i == ":"
            dot_found += i == "."
            if last_block and block != last_block:
                print("ERROR")
                return
            if block > 0:
                parts_count += 1
            last_block, block = block, 0
            continue
        if i.isalnum():
            if i.upper() not in "0123456789ABCDEF":
                print("ERROR")
                return
            block += 1
        else:
            print("ERROR")
            return

    if check_errors(dash_found, colon_found, dot_found, last_block, parts_count):
        return

    if dash_found:
        print('VALID 1')
    elif colon_found:
        print('VALID 2')
    elif dot_found:
        print('VALID 3')
    else:
        print("ERROR")

main()
