"""Docstring"""
def main():
    """Bro thinks he is JoJo TwT.."""
    seconds = int(input())
    punches = int(input())
    punched = 0
    for sec in range(1,seconds+1):
        # ペガサスローリングクラッシュ
        if punched >= punches:
            punched += 12*(seconds-sec)
            break
        # ペガサス流星拳 & ペガサス彗星拳
        if not sec%6:
            punched += 1
        elif not sec%2:
            punched += 165

    print(punched)

main()
