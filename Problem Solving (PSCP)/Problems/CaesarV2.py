"""Docstring"""
def main():
    """hacker man ~ Hacker man! Again!"""
    text = input()
    result = ""
    words = ["what", "when", "why", "which", "this", "there", "where", "the",
             "is", "am", "are","you", "we", "they", "he", "she", "it"]
    for shift in range(26):
        result = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += char

        words_in_result = result.split(" ")
        for w in words_in_result:
            if w in words:
                print(result)
                return
main()
