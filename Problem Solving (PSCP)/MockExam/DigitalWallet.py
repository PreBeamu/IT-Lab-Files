"""Digital Wallet."""


def main():
    """Return epic msg if user is valid for moneh."""
    name = input()
    is_thai = input()
    valid_address = input()
    age = float(input())
    salary = float(input())
    money = float(input())
    # Check Input
    if is_thai == "False" or is_thai == "No":
        is_thai = False
    elif is_thai == "True" or is_thai == "Yes":
        is_thai = True
    if valid_address == "False" or valid_address == "No":
        valid_address = False
    elif valid_address == "True" or valid_address == "Yes":
        valid_address = True
    # Not Valid
    if age < 16:
        print(f"Unfortunately, {name} is not qualified.")
        return
    if not is_thai or not valid_address:
        print(f"Unfortunately, {name} is not qualified.")
        return
    if money > 500000:
        print(f"Unfortunately, {name} is not qualified.")
        return
    if salary > 840000:
        print(f"Unfortunately, {name} is not qualified.")
        return
    # Valid
    print(f"Congratulations! {name} is qualified to receive", end=" ")
    print("a digital wallet amount of 10,000 baht,", end=" ")
    print("sponsored by all taxpayers in Thailand.")


main()
