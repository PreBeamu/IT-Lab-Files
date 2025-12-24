"""Least Vowel."""

def count_saraa(word):
    """Return saraa counts."""
    vowels = "aeiou"
    word = word.lower()
    return sum(i in vowels for i in word) \
        if any(i.isalpha() for i in word) else float("inf")


def main():
    """Return the answer."""
    msg = input().split()
    min_le = float("inf")
    answer = []
    for word in msg:
        founded = count_saraa(word)
        if founded < min_le:
            min_le = founded
            answer = []
        if founded <= min_le:
            x = ""
            for i in word:
                x += i if i.isalpha() else ""
            answer.append(x)
    print(" ".join(answer))


main()
