"""Docstring"""
def main():
    """How come they can't climb the staris..
    We don't have an elevator here!"""
    highest = int(input())
    steps = int(input())
    steps_height = []
    for _ in range(steps):
        height = int(input())
        steps_height.append(height)

    current_step = 0
    height_sum = 0
    for num in steps_height:
        if num > highest:
            print("NO")
            return
        if height_sum + num > highest:
            current_step += 1
            height_sum = num
        else:
            height_sum += num
    if height_sum > 0:
        current_step += 1

    print(current_step)

main()
