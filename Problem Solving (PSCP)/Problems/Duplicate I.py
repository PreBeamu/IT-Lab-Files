"""Docstring"""
def main():
    """WHO DID IT!"""
    group1,group2 = int(input()),int(input())
    students1,students2 = [],[]
    for _ in range(group1):
        x = int(input())
        students1.append(x)
    for _ in range(group2):
        x = int(input())
        students2.append(x)
    # Check for Duplicate IDs
    picked = max(group1,group2)
    duplicate = []
    for i in range(picked):
        if picked == group1:
            if students1[i] in students2:
                duplicate.append(students1[i])
        elif picked == group2:
            if students2[i] in students1:
                duplicate.append(students2[i])
    if not duplicate:
        print("Nope")
        return
    for txt in sorted(duplicate)[::-1]:
        print(txt)
main()
