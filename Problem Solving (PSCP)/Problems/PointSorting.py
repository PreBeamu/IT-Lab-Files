"""Docstring"""
def main():
    """Wah! This seems hard to code!"""
    data_amount = int(input())
    data_points = []
    for _ in range(data_amount):
        n = int(input())
        points_list = []
        for _ in range(n):
            point = input()
            points_list.append(point.split())
        points_list.sort(key=lambda p: (int(p[0]) + int(p[1]), -int(p[1])))
        data_points.append(points_list)
    for data in data_points:
        for p in data:
            print(" ".join(p))

main()
