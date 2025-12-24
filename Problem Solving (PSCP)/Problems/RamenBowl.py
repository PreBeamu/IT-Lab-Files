"""docstring"""
def main():
    """docsrting"""
    pate = int(input())
    stack = []
    nab = []
    for _ in range(pate):
        number = int(input())
        stack.append(number)
    for i in stack:
        nab.append(stack.count(i))
    print(max(nab))

main()
