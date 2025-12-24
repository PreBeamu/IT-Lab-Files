"""Docstring"""
def main():
    """Giraffe long neck."""
    amount = int(input())
    height = []
    full = 0
    for _ in range(amount):
        x = int(input())
        height.append(x)
    for i in range(amount):
        left,right = -1,-1
        current = height[i]
        if not i and amount>1:
            right = height[i+1]
        elif i+1 == len(height) and amount>1:
            left = height[i-1]
        else:
            if amount>1:
                right = height[i+1]
                left = height[i-1]
        if left < current > right:
            full += 1
    print(full)
main()
