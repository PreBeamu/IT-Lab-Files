"""Docstung"""

def main():
    "Main func!"
    W, H = map(int, input().split())
    input()
    x_cuts = list(map(int, input().split()))
    y_cuts = list(map(int, input().split()))
    x_cuts = [0] + x_cuts + [W]
    y_cuts = [0] + y_cuts + [H]

    widths = [x_cuts[i+1] - x_cuts[i] for i in range(len(x_cuts) - 1)]
    heights = [y_cuts[i+1] - y_cuts[i] for i in range(len(y_cuts) - 1)]
    areas = [w * h for w in widths for h in heights]
    areas.sort(reverse=True)

    print(areas[0])
    print(areas[1])

main()
