"""Docstring"""
def main():
    """Big N letter!"""
    m = int(input())
    for layer in range(m):
        print("*",end="")
        spaces = m-2
        e = ""
        if 0 < layer < m-1:
            spaces = layer-1
            e = (" "*spaces)+"*"
            print(e,end="")
        spaces = (m-2)-len(e)
        print(" "*spaces,end="")
        print("*")

main()
