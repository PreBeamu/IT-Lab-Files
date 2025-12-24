"""Docstring"""
def main():
    """SEQUENCES give me PTSD!!"""
    num = int(input())
    text = ""
    text_to_show = []
    num_before = 0
    for i in range(1,num+1):
        if num_before:
            for x in range(1,num_before+1):
                text += f"{x:02d} "
        text += f"{i:02d} "
        if num_before:
            for x in range(num_before,0,-1):
                text += f"{x:02d} "
        text_to_show.append(text)
        num_before = i
        text = ""

    max_width = len(text_to_show[-1])
    for t in text_to_show:
        spaces = (max_width - len(t)) // 2
        print(" " * spaces + t.rstrip())

main()
