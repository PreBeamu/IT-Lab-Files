"""Docstring"""
def main():
    """Dart gaem."""
    dart = int(input())
    hit = []
    score = 0
    for _ in range(dart):
        point = input()
        hit.append(point.split())
    for pos in hit:
        x,y = int(pos[0]),int(pos[1])
        radius = ((x**2)+(y**2))**0.5
        if radius <= 2:
            score += 5
        elif radius <= 4:
            score += 4
        elif radius <= 6:
            score += 3
        elif radius <= 8:
            score += 2
        elif radius <= 10:
            score += 1
    print(score)
main()
