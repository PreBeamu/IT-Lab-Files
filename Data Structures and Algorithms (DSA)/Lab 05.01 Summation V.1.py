def summation(n):
    count = 0
    for i in range(n):
        count += i
    count += n
    return count

print(summation(int(input())))