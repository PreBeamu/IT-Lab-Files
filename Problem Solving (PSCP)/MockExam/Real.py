"""Real."""


def main():
    """Return decoded 7-segment."""
    result = ""
    error_flag = False
    for _ in range(3):
        a, b, c, d = input(), input(), input(), input()
        e, f, g, dp = input(), input(), input(), input()
        data = (a+b+c+d+e+f+g).replace("on", "1").replace("off", "0")
        num_0, num_1, num_2 = "1111110", "0110000", "1101101"
        num_3, num_4, num_5 = "1111001", "0110011", "1011011"
        num_6, num_7, num_8 = "1011111", "1110000", "1111111"
        num_9 = "1111011"
        if data == num_0:
            result += "0"
        elif data == num_1:
            result += "1"
        elif data == num_2:
            result += "2"
        elif data == num_3:
            result += "3"
        elif data == num_4:
            result += "4"
        elif data == num_5:
            result += "5"
        elif data == num_6:
            result += "6"
        elif data == num_7:
            result += "7"
        elif data == num_8:
            result += "8"
        elif data == num_9:
            result += "9"
        else:
            error_flag = True
        if dp == "on":
            result += "."
            if result.count(".") > 1:
                error_flag = True
    if error_flag:
        print("Error")
        return
    print(f"{float(result):.2f}")


main()
