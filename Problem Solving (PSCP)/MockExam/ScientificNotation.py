"""Scientific Notation."""


def main():
    """Return an answer of a number or scientific notation."""
    data = input().strip()
    if "x 10^" in data:
        sign = ""
        if data[0] == "-":
            sign = data[0]
            data = data[1:]
        pos = data.find("x 10^")
        num = data[:pos].strip()
        power = int(data[pos+5:].strip())
        # Getting dot position.
        if "." in num:
            dot_pos = num.find(".")
            digits = num.replace(".", "")
        else:
            dot_pos = len(num)
            digits = num
        # Calculate and adding new dot.
        new_dot = dot_pos + power
        if new_dot <= 0:
            result = "0." + ("0" * (-new_dot)) + digits
        elif new_dot >= len(digits):
            result = digits + ("0" * (new_dot - len(digits)))
        else:
            result = digits[:new_dot] + "." + digits[new_dot:]
        print(sign+result)
        return
    # Numbers to notation.
    num = data
    sign = ""
    if num[0] == "-":
        sign = num[0]
        num = num[1:]
    if "." in num:
        dot_pos = num.find(".")
        int_part = num[:dot_pos].lstrip("0")
        frac_part = num[dot_pos+1:]
    else:
        int_part = num.lstrip("0")
        frac_part = ""

    if not int_part.strip("0") and not frac_part.strip("0"):
        print("0")
        return
    if int_part and int_part.strip("0"):
        power = len(int_part) - 1
        digits = int_part + frac_part
    else:
        i = 0
        while i < len(frac_part) and frac_part[i] == "0":
            i += 1
        power = -(i + 1)
        digits = frac_part[i:]
        digits = digits + frac_part[i+len(digits):]

    if frac_part == "":
        while len(digits) > 1 and digits[-1] == "0":
            digits = digits[:-1]
    if len(digits) == 1:
        sci_num = digits
    else:
        sci_num = digits[0] + "." + digits[1:]

    print(sign + sci_num + " x 10^" + str(power))


main()
