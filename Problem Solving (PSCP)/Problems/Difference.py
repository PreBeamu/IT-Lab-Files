"""Docstung"""

def main():
    """Main func!"""
    n = int(input())
    m = int(input())
    set_a = set()
    set_b = set()

    for _ in range(n):
        element = int(input())
        set_a.add(element)

    for _ in range(m):
        element = int(input())
        set_b.add(element)

    result_set = set_a - set_b
    sorted_result = sorted(list(result_set))
    e = [str(i) for i in sorted_result]
    print(" ".join(e))

main()
