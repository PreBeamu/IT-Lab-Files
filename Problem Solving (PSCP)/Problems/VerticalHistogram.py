"""Docstring"""
def main():
    """Hard Histogram!"""
    msg = input()
    letters = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    sorted_letters = []
    graph_height = 0
    # Count Letters and sort.
    for i in msg:
        letters[i] = msg.count(i)
    for x in alphabet:
        if x in letters:
            sorted_letters.append(x)
            if letters[x] > graph_height:
                graph_height = letters[x]
    # Histogram!
    for i in range(graph_height,0,-1):
        txt = ""
        for x in sorted_letters:
            if letters[x] >= i:
                txt += "* "
            else:
                txt += "  "
        if i <= 9:
            print((" "+str(i)+"  "+txt).rstrip())
        else:
            print(( str(i)+"  "+txt).rstrip())
    print("    "+" ".join(sorted_letters))
main()
