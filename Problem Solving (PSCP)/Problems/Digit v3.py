"""Docstring"""
def main():
    """How much is this? But in number!"""
    read = input().split()
    sum_num = 0
    queue_num = 0
    numbers = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    if len(read) == 1:
        print(numbers[read[0]])
        return
    for n in read:
        if n == "hundred":
            queue_num *= 100
        elif n == "thousand":
            sum_num += queue_num * 1000
            queue_num = 0
        else:
            queue_num += numbers[n]
    print(sum_num+queue_num)
main()
