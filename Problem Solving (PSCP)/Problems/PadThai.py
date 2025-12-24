"""Docstring"""
def main():
    """Pad Thai! We're cooking chef.."""
    b_ingredients = ["Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp","Bean Sprouts",
                   "Noodle","Chives","Lime","Egg","Oil","Peanuts"]
    b_taste = ["Sweet","Sour","Salty"]
    ingredients = ["Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp","Bean Sprouts",
                   "Noodle","Chives","Lime","Egg","Oil","Peanuts"]
    taste = ["Sweet","Sour","Salty"]
    weird_ingre = []
    weird_taste = []
    while True:
        x = input()
        if x == "End":
            break
        if x in b_ingredients:
            if x in ingredients:
                ingredients.remove(x)
            continue
        if x in b_taste:
            if x in taste:
                taste.remove(x)
            continue
        if x == "Cook" or "Cook" not in weird_ingre:
            weird_ingre.append(x)
        if x != "Cook" and "Cook" in weird_ingre:
            weird_taste.append(x)
    weird_ingre.remove("Cook")
    if weird_ingre:
        print("This is not Pad Thai!!!")
        return
    if ingredients:
        print("This is bad!")
        return
    if taste or weird_taste:
        print("Not Bad...")
        return
    print("Delicious!")
main()
