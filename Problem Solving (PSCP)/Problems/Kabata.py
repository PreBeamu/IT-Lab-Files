"""Docstring"""
def main():
    """Kabatatatatatatatbakka!"""
    num = int(input())
    result = ""
    for _ in range(num):
        msg = input()
        while "ta" in msg or "ka" in msg or "ba" in msg or "bakka" in msg:
            if "baka" in msg:
                msg += " "
            msg = msg.replace("bakka","")
            msg = msg.replace("ta","")
            msg = msg.replace("ka","")
            msg = msg.replace("ba","")
        result += "no " if msg else "yes "
    rl = ""
    for txt in result:
        if txt == " ":
            print(rl)
            rl = ""
            continue
        rl += txt
main()
