"""Docstring"""
def main():
    """Fizz Buzz?.. FISH BUS!"""
    num = int(input())
    numbers = []
    for i in range(1,num+1):
        if not i%3 or not i%5:
            numbers.append(i)
    print(sum(numbers))

main()
