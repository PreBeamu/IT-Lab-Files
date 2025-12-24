"""Docstring"""
def main():
    """I like the fact that these oranges in the images are so rounded!"""
    layers = int(input())
    sold = int(input())
    remaining_layers = layers
    for i in range(1,layers+1):
        oranges_in_layer = i**2
        if sold >= oranges_in_layer:
            sold -= oranges_in_layer
            remaining_layers -= 1
        else:
            break
    print(remaining_layers)

main()
