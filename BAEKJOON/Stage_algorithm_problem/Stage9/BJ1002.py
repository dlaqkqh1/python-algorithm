from math import sqrt

cnt = int(input())

for x in range(cnt):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dot_distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    if dot_distance == 0 and r1 == r2:
        print(-1)
    elif dot_distance < abs(r1 - r2) or dot_distance > r1 + r2:
        print(0)
    elif dot_distance == r1 + r2 or dot_distance == abs(r1 - r2):
        print(1)
    else:
        print(2)
