"""Docstring"""
def main():
    """Solar System!"""
    solar = input()+" "
    first,last,current = "","",""
    hot,cool = "",""
    sun_found = False
    f_spaces,l_spaces = -1,0
    # Loop Through the space!
    for letter in solar:
        if letter == " ":
            if not sun_found:
                f_spaces += 1
            else:
                l_spaces += 1
            if not first:
                first = current
            if last == "Sun":
                hot += current
            if current == "Sun":
                sun_found = True
                hot += last+" "
            last = current
            current = ""
            continue
        current += letter
    # Checking for Cool planets!
    if first != "Sun" and first not in hot and f_spaces>=l_spaces:
        cool += first+" "
    if last != "Sun" and last not in hot and l_spaces>=f_spaces:
        cool += last+" "
    if solar.strip().count(" ") <= 2 and f_spaces==l_spaces:
        print("Hot:",hot.lstrip().rstrip())
        print("Cool:",hot.lstrip().rstrip())
        return
    if solar.strip().count(" ") < 2:
        print("Hot:",hot.lstrip().rstrip())
        print("Cool:",hot.lstrip().rstrip())
        return
    print("Hot:",hot.lstrip().rstrip())
    print("Cool:",cool.lstrip().rstrip())
main()
