"""Docstring"""
import json

def getMih(x_list):
    cur_mih = float('inf')
    for i in x_list:
        if float(i) < cur_mih:
            cur_mih = float(i)
    return cur_mih

def getMah(x_list):
    cur_mah = 0
    for i in x_list:
        if float(i) > cur_mah:
            cur_mah = float(i)
    return cur_mah

def main():
    """Main func!"""
    my_list = json.loads(input())
    avg = sum(my_list)/len(my_list)
    my_tuple = (round(getMah(my_list),2),round(getMih(my_list),2),round(avg,2))
    print(my_tuple)

main()
