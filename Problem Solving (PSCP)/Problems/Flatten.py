"""Docstring"""
def main():
    """Super Flat!"""
    in_list = input().replace("[","").replace("]","").replace(" ","").split(',')
    result = []
    for i in in_list:
        result.append(int(i))
    print(sorted(result,reverse=True))
main()
