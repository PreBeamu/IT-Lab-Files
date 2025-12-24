"""Docstring"""
def main():
    """Pig Big Pig!"""
    amount = int(input())
    pigs = input().split()
    max_pig = []
    for i in range(0,amount*2,2):
        max_pig.append(str(max(int(pigs[i]),int(pigs[i+1]))))
    sum_pig = 0
    for i in max_pig:
        sum_pig += int(i)
    if amount > 1:
        print(" + ".join(max_pig),"=",sum_pig)
    else:
        print(sum_pig)
main()
