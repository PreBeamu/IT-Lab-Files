"""Docstring"""
def main():
    """Boba.."""
    in1 = input().split()
    boba_type = in1[0]
    boba_amount = int(in1[1])
    in2 = input().split()
    tea_type = in2[0]
    sugar_level = int(in2[1])
    tea_amount = int(in2[2])

    tea_energy = {
        "R": {1: 12, 2: 18, 3: 25},
        "T": {1: 15, 2: 20, 3: 30},
        "M": {1: 10, 2: 15, 3: 20}
    }
    boba_energy = {
        "H": 5,
        "O": 3,
        "J": 2
    }

    energy = tea_energy[tea_type][sugar_level] * tea_amount
    energy += boba_energy[boba_type] * boba_amount
    print(energy)

main()
