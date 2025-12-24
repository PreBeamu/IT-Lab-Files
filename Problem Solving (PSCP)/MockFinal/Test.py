""" Diabete """
import json
def main():
    """ main """
    txt = input()
    data = json.loads(txt)

    exceed = 0
    notexceed = 0

    for i in data:# name age sugar
        if 6 <= int(i["age"]) <= 13 or 25 <= int(i["age"]) <= 60 or 60 < int(i["age"]):
            if int(i["sugar"]) <= 16:
                print(f"{i["name"]} ({int(i["age"])}): eat sugar within the limit")
                notexceed += 1
            elif int(i["sugar"]) > 16:
                print(f"{i["name"]} ({int(i["age"])}): eat too much sugar")
                exceed += 1
            else:
                print(f"{i["name"]} ({int(i["age"])}): error")

        elif 14 <= int(i["age"]) <= 25:
            if int(i["sugar"]) <= 24:
                print(f"{i["name"]} ({int(i["age"])}): eat sugar within the limit")
                notexceed += 1
            elif int(i["sugar"]) > 24:
                print(f"{i["name"]} ({int(i["age"])}): eat too much sugar")
                exceed += 1
            else:
                print(f"{i["name"]} ({int(i["age"])}): error")

        else:
            print(f"{i["name"]} ({int(i["age"])}): error")

    print()
    print(f"Exceed: {exceed}")
    print(f"Not Exceed: {notexceed}")

main()
