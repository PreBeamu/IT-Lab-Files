"""Docstring"""
def main():
    """Mathicc MN!"""
    m = int(input())
    n = int(input())
    matrix = []
    num_list = []
    for i in range(m*n):
        num = int(input())
        if len(num_list) == n:
            matrix.append(num_list)
            num_list = []
        num_list.append(str(num))
        if len(num_list) == n:
            matrix.append(num_list)
            num_list = []
    for i in range(m):
        print(" ".join(matrix[i]))

main()
