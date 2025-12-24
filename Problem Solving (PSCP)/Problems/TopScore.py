"""Docstring"""
def main():
    """I want big score, Me study hard!"""
    students = int(input())
    top_students = 0
    most_score = 0

    for _ in range(students):
        score = int(input())
        if score > most_score:
            most_score = score
            top_students = 1
        elif score == most_score:
            top_students += 1

    print(most_score)
    print(top_students)

main()
