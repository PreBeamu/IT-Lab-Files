"""Docstung"""

def main():
    "Main func!"
    amount = int(input())
    data = {}

    for _ in range(amount):
        x = input()
        name = ''.join(i for i in x if i.isalpha())
        data[name] = {}
        data[name]["score"] = ' '.join(x.replace(name+" ","").split())
        data[name]["medals"] = [int(i) for i in x.replace(name+" ","").split()]
        data[name]["sum"] = sum(int(i) for i in x.replace(name+" ","").split())

    places = sorted(
        data,
        key=lambda name: (
            -data[name]["medals"][0],
            -data[name]["medals"][1],
            -data[name]["medals"][2],
            name
        )
    )

    current = 1
    display_p, skipped = 0, 0
    last_score = ""
    for i in places:
        display_p += 1
        if data[i]["score"] == last_score:
            display_p -= 1
            skipped += 1
        elif skipped:
            display_p = current
            skipped = 0
        print(display_p,i,data[i]["score"],data[i]["sum"])
        last_score = data[i]["score"]
        current += 1

main()
