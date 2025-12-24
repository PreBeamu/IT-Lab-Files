"""Docstring"""
def main():
    """SEQUENCES give me PTSD!!"""
    num = int(input())
    # Top
    min_num = 1
    for _ in range(num-1):
        top_text = []
        for i in range(1,num+1):
            top_text.append(f"{min(i,min_num):02d}")
        for i in range(num-1,0,-1):
            top_text.append(f"{min(i,min_num):02d}")
        min_num += 1
        print(" ".join(top_text))
    # Middle
    middle_text = []
    for i in range(1,num):
        middle_text.append(f"{i:02d}")
    middle_text.append(f"{num:02d}")
    for i in range(num-1,0,-1):
        middle_text.append(f"{i:02d}")
    print(" ".join(middle_text))
    # Bottom
    min_num = num-1
    for _ in range(num-1):
        top_text = []
        for i in range(1,num+1):
            top_text.append(f"{min(i,min_num):02d}")
        for i in range(num-1,0,-1):
            top_text.append(f"{min(i,min_num):02d}")
        min_num -= 1
        print(" ".join(top_text))

main()
