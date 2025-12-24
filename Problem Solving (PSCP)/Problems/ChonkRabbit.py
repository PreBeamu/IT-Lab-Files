"""Docstring"""
def main():
    """Chonky Bunnies!"""
    bunnies = int(input())
    bunnies_data = {}
    for _ in range(bunnies):
        data = input()
        name = data.split(" ")[0]
        weight = int(data.split(" ")[1])
        bunnies_data[name] = weight
    chonky = 0
    most_chonky = ["",0]
    for nameb,weightb in bunnies_data.items():
        if weightb > most_chonky[1]:
            most_chonky[0] = nameb
            most_chonky[1] = weightb
        if weightb > 15:
            chonky += 1
    print(chonky)
    print(most_chonky[0],most_chonky[1])
main()
