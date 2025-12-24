"""Docstring"""
def main():
    """Aww.. Poor tuple.."""
    tuple_in = tuple(input().split())
    look_for = input().strip()
    count_look = tuple_in.count(look_for)
    first_index = tuple_in.index(look_for)
    for _ in range(count_look):
        print(" ".join([str(first_index)] * count_look))

main()
