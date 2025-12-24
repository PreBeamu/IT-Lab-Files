"""Docstring"""
def main():
    """main Func!"""
    income = int(input())
    tax = 0.0
    if income > 60000:
        tax += (income - 60000) * 0.25
        income = 60000
    if income > 30000:
        tax += (income - 30000) * 0.20
        income = 30000
    if income > 10000:
        tax += (income - 10000) * 0.15
        income = 10000
    if income > 0:
        tax += income * 0.10
    print(round(tax, 2))

main()
