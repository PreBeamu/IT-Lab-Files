"""Docstring"""
def main():
    """Really? A password generator?"""
    name = input()
    last_name = input()
    age = input()

    password = ""
    if len(name) >= 5 and len(last_name) >= 5:
        password = name[0:2]+last_name[-1]+age[-1]
    else:
        password = name[0]+age+last_name[-1]
    print(password)

main()
