"""Docstring"""
import json

def main():
    """Last one stand!!"""
    my_list = json.loads(input())
    for i in my_list:
        print(str(i)[-1:])
main()
