def get_max_num(num):
    global max_num

    if num == 0:
        max_num = 1
    elif num == 1:
        max_num = 7
    else:
        max_num = max_num + 6 * num


num = int(input())
max_num = 1

for x in range(1, 20000):
    if max_num >= num:
        print(x)
        break
    else:
        get_max_num(x)
