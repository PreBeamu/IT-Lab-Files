"""Docstring"""
import json

def main():
    """Pick them!!"""
    my_list = json.loads(input())
    even_nums = 0
    for i in my_list:
        if not int(i)%2:
            print(i)
            even_nums += 1
    if not even_nums:
        print("Nope")
main()
