"""Docstring"""
def main():
    """I saw that one video that has a man boxing a kangaroo!"""
    A = int(input())
    B = int(input())
    C = int(input())
    positions = [A, B, C]

    max_jumpable = max(positions[1] - positions[0], positions[2] - positions[1]) - 1
    print(max_jumpable)
main()
