"""Docstring"""
def main():
    """Good to know that none of these guys are missing a leg."""
    animals = int(input())
    legs = int(input())

    if legs < animals*2 or legs > animals*4 or (legs - 2*animals) % 2:
        print("Impossible")
    else:
        bunnies = (legs - 2*animals)//2
        birds = animals-bunnies
        print(bunnies,birds)

main()
