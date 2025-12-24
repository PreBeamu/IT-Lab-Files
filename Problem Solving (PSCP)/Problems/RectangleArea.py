"""Docstring"""
def main():
    """You stepped inside my area you shall be gone!"""
    A_rect = input()
    A_width = int(A_rect.split()[2])
    A_height = int(A_rect.split()[3])
    A_Ll = (int(A_rect.split()[0]),int(A_rect.split()[1]))
    A_Ur = (int(A_rect.split()[0])+A_width,int(A_rect.split()[1])+A_height)

    B_rect = input()
    B_width = int(B_rect.split()[2])
    B_height = int(B_rect.split()[3])
    B_Ll = (int(B_rect.split()[0]),int(B_rect.split()[1]))
    B_Ur = (int(B_rect.split()[0])+B_width,int(B_rect.split()[1])+B_height)

    overlap_left = max(A_Ll[0], B_Ll[0])
    overlap_right = min(A_Ur[0], B_Ur[0])
    overlap_bottom = max(A_Ll[1], B_Ll[1])
    overlap_top = min(A_Ur[1], B_Ur[1])

    if A_Ll[0] < B_Ur[0] and B_Ll[0] < A_Ur[0] and A_Ll[1] < B_Ur[1] and B_Ll[1] < A_Ur[1]:
        overlap_area = (overlap_right - overlap_left) * (overlap_top - overlap_bottom)
        print(overlap_area)
    else:
        print("no overlapping")

main()
