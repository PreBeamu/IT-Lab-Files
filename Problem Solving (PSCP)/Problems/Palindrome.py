"""Docstring"""
def main():
    """Palindrome! We can read stuff backwards!"""
    num = int(input())
    time = input().replace(":","")
    hr = int(time[:1]) if len(time) < 4 else int(time[:2])
    m = int(time[1:]) if len(time) < 4 else int(time[2:])
    palindrome = 0
    while palindrome < num:
        m += 1
        hr %= 24
        if m == 60:
            m = 0
            hr += 1
            hr %= 24
        if hr < 10:
            if str(hr) == f"{m:02d}"[-1]:
                print(str(hr)+":"+f"{m:02d}")
                palindrome += 1
        else:
            if str(hr) == f"{m:02d}"[::-1]:
                print(str(hr)+":"+f"{m:02d}")
                palindrome += 1

main()
