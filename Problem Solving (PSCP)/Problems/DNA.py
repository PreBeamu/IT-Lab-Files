"""Docstring"""
def main():
    """What?.. We're not blood related?"""
    dna1 = input()
    dna2 = input()
    if dna1.replace("A","").replace("C","").replace("G","").replace("T",""):
        print("Error")
        return
    if dna2.replace("A","").replace("C","").replace("G","").replace("T",""):
        print("Error")
        return
    len1, len2 = len(dna1), len(dna2)
    match = ""
    for i in range(len1):
        i_index = 0
        for x in range(len2):
            if i+i_index<len1 and (dna1[i+i_index] == dna2[x]):
                i_index += 1
                match += dna2[x]
            else:
                if match and not match.endswith("#"):
                    match += "#"
        if match and not match.endswith("#"):
            match += "#"
    text = ""
    result = ""
    for i in match:
        if i == "#":
            if len(text) > len(result):
                result = text
            text = ""
            continue
        text += i
    if not result:
        print("None")
        return
    print(result)
main()
