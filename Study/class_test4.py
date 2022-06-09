import math
 
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

for num in range(len(p)-1):
    x2 = math.pow(p[num+1].x - p[num].x, 2)
    y2 = math.pow(p[num+1].y - p[num].y, 2)
    length += math.sqrt(x2 + y2)

print(length)