"""Docstring"""
def main():
    """NO! 456 Why'd you do that!"""
    team_A_Power = 0
    for _ in range(10):
        power = int(input())
        team_A_Power += power

    team_B_Power = 0
    for _ in range(10):
        power = int(input())
        team_B_Power += power

    if team_A_Power > team_B_Power:
        print("B")
    elif team_B_Power > team_A_Power:
        print("A")
    elif team_B_Power == team_A_Power:
        print("AB")

main()
