x_list = []
y_list = []
for x in range(3):
    x, y = input().split()
    x_list.append(x)
    y_list.append(y)

print(min(x_list, key=x_list.count), min(y_list, key=y_list.count))
