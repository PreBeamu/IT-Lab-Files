"""Docstring"""

def main():
    """Main func!"""
    scores = [int(input()) for _ in range(4)]
    scores = sorted(scores,reverse=True)
    scores.pop()
    print(sum(scores))

main()
