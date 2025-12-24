"""Docstring"""

def main():
    """Dang it! I'm LATE!!"""
    directions = input()
    arrows_U = [
        [" "," ","*"," ","  "],
        [" ","*","*","*","  "],
        ["*"," ","*"," ","* "],
        [" "," ","*"," ","  "],
        [" "," ","*"," ","  "],
    ]
    arrows_D = [
        [" "," ","*"," ","  "],
        [" "," ","*"," ","  "],
        ["*"," ","*"," ","* "],
        [" ","*","*","*","  "],
        [" "," ","*"," ","  "],
    ]
    arrows_R = [
        [" "," ","*"," ","  "],
        [" "," "," ","*","  "],
        ["*","*","*","*","* "],
        [" "," "," ","*","  "],
        [" "," ","*"," ","  "],
    ]
    arrows_L = [
        [" "," ","*"," ","  "],
        [" ","*"," "," ","  "],
        ["*","*","*","*","* "],
        [" ","*"," "," ","  "],
        [" "," ","*"," ","  "],
    ]
    # Connect all the Arrows!
    result = [[],[],[],[],[]]
    def check_arrow(direc):
        """Check directions."""
        if direc == "U":
            for i in range(5):
                for x in arrows_U[i]:
                    result[i].append(x)
        elif direc == "D":
            for i in range(5):
                for x in arrows_D[i]:
                    result[i].append(x)
        elif direc == "L":
            for i in range(5):
                for x in arrows_L[i]:
                    result[i].append(x)
        elif direc == "R":
            for i in range(5):
                for x in arrows_R[i]:
                    result[i].append(x)
    for direc in directions:
        check_arrow(direc)
    for i in range(5):
        print("".join(result[i]))
main()
