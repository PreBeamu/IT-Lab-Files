"""Docstring"""
def main():
    """That one meme with 2,865,784 lines of code for chess!"""
    row1 = input()
    row2 = input()
    row3 = input()

    line1 = row1
    line2 = row2
    line3 = row3
    line4 = row1[0] + row2[0] + row3[0]
    line5 = row1[1] + row2[1] + row3[1]
    line6 = row1[2] + row2[2] + row3[2]
    line7 = row1[0] + row2[1] + row3[2]
    line8 = row1[2] + row2[1] + row3[0]

    if line1[0] != "-" and line1[0] == line1[1] == line1[2]:
        print(line1[0], "WIN")
    elif line2[0] != "-" and line2[0] == line2[1] == line2[2]:
        print(line2[0], "WIN")
    elif line3[0] != "-" and line3[0] == line3[1] == line3[2]:
        print(line3[0], "WIN")
    elif line4[0] != "-" and line4[0] == line4[1] == line4[2]:
        print(line4[0], "WIN")
    elif line5[0] != "-" and line5[0] == line5[1] == line5[2]:
        print(line5[0], "WIN")
    elif line6[0] != "-" and line6[0] == line6[1] == line6[2]:
        print(line6[0], "WIN")
    elif line7[0] != "-" and line7[0] == line7[1] == line7[2]:
        print(line7[0], "WIN")
    elif line8[0] != "-" and line8[0] == line8[1] == line8[2]:
        print(line8[0], "WIN")
    else:
        print("DRAW")

main()
