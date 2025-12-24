"""Docstring"""
def main():
    """We're aligning this word."""
    board_size = int(input())
    align = input().lower()
    text = input()
    if align == "center":
        if not (board_size-len(text))%2:
            print(text.center(board_size))
        else:
            print((" "*int((board_size-len(text))/2+1))+text+(" "*int((board_size-len(text))/2)))
    elif align == "left":
        print(text.ljust(board_size))
    elif align == "right":
        print(text.rjust(board_size))

main()
