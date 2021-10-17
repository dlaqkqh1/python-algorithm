from math import pi
num = int(input())

u_circle = round(num * num * pi, 6)
t_circle = (num * 2) * (num * 2) - (num * num * 2)

print(u_circle)
print(t_circle)
