"""Docstring"""
def main():
    """SEQUENCES give me PTSD!!"""
    num = int(input())
    digits = 1
    text = ""
    for _ in range(num):
        for x in range(1,digits+1):
            if x != digits:
                text += (f"{x:02d} ")
            else:
                text += f"{x:02d} "
        print(("   "*(num-digits)+text).rstrip())
        text = ""
        digits += 1

main()
