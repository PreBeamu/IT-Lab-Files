"""Docstring"""
def main():
    """SEQUENCES give me PTSD!!"""
    num = int(input())
    operators = []
    base_list = []
    for _ in range(num*2-1):
        operators.append("+")
        base_list.append("")

    def funny_math(column,i):
        """What the..."""
        # Check numbers condition
        if base_list[column]:
            x = int(base_list[column])
            expected_num = x-1 if operators[column] == "-" else x+1
        else:
            expected_num = i
        base_list[column] = f"{expected_num:02d}"
        # Funny stuff here
        if int(base_list[column]) == num:
            operators[column] = "-"
        elif int(base_list[column]) == 1:
            operators[column] = "+"

    # Top
    top_texts = []
    for _ in range(num-1):
        column = 0
        for i in range(num,1,-1):
            funny_math(column,i)
            column += 1
        for i in range(1,num+1):
            funny_math(column,i)
            column += 1
        top_texts.append(base_list.copy())
    for txt in top_texts:
        print(" ".join(txt))
    # Middle
    middle_text = []
    for i in range(1,num):
        middle_text.append(f"{i:02d}")
    middle_text.append(f"{num:02d}")
    for i in range(num-1,0,-1):
        middle_text.append(f"{i:02d}")
    print(" ".join(middle_text))
    # Bottom
    top_texts.reverse()
    for txt in top_texts:
        print(" ".join(txt))

main()
