"""Docstring"""
def main():
    """US Interstate Number System!"""
    num = input()
    if not int(num) or num[-1] not in ["0","5"]:
        print("Others")
        return
    num = str(int(num))
    road_type = ""
    direction = ""
    zone_num = num
    if 1 <= len(num) <= 2:
        road_type = "Major Interstate"
        if num[-1] == "0":
            direction = "Horizontal"
        elif num[-1] == "5":
            direction = "Vertical"
        else:
            print("Others")
            return
    elif len(num) == 3:
        road_type = "Minor Interstate"
        zone_num = str(int(num[1:]))
        if zone_num == "0":
            print("Others")
            return
        if int(num[0])%2:
            direction = "Odd"
        else:
            direction = "Even"
    else:
        print("Others")
        return
    print(direction,road_type)
    print("I-"+zone_num)
main()
